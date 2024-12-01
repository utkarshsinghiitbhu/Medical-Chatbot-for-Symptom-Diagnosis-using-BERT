from flask import Flask, request, jsonify, render_template
import torch
from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd
import os

# Load the saved model, tokenizer, and label mapping
MODEL_DIR = "./saved_model"

try:
    print("Loading model and tokenizer...")
    model = BertForSequenceClassification.from_pretrained(MODEL_DIR)
    tokenizer = BertTokenizer.from_pretrained(MODEL_DIR)
    df_label = pd.read_pickle(os.path.join(MODEL_DIR, "df_label.pkl"))
    print("Model and tokenizer loaded successfully!")
except Exception as e:
    raise FileNotFoundError(f"Could not load model or required files: {e}")

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# Initialize Flask app
app = Flask(__name__)

# Home route (renders the chatbot interface)
@app.route("/")
def home():
    return render_template("index.html")

# API route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        symptoms = data.get("symptoms", "")
        if not symptoms:
            return jsonify({"error": "No symptoms provided"}), 400

        # Preprocess input
        inputs = tokenizer(
            symptoms,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=128
        ).to(device)

        # Perform inference
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits, dim=1).item()
        predicted_label = df_label.iloc[predicted_class]["intent"]

        return jsonify({"predicted_label": predicted_label})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
