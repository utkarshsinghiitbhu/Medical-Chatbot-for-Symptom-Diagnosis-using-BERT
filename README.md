# Medical Symptom Detector

A web-based application built using **Flask**, **PyTorch**, and **Transformers** to detect medical symptoms based on user input. This tool can be used for basic intent detection in medical applications like chatbots.

---

## **Features**

- **BERT Model**: Utilizes a pre-trained BERT model for symptom classification.
- **Flask API**: Backend developed with Flask for seamless data processing and model inference.
- **Interactive Web Interface**: Users can enter symptoms via a user-friendly web interface to get predictions.
- **Responsive Design**: A clean, responsive interface styled with CSS.
- **JSON API Endpoint**: Allows integration with other tools through the `/predict` endpoint.

---

## **Project Structure**


Here’s a README.md file tailored for your project based on the files and structure provided. This document is designed to clearly describe your project for GitHub.

README.md
markdown
Copy code
# Medical Symptom Detector

A web-based application built using **Flask**, **PyTorch**, and **Transformers** to detect medical symptoms based on user input. This tool can be used for basic intent detection in medical applications like chatbots.

---

## **Features**

- **BERT Model**: Utilizes a pre-trained BERT model for symptom classification.
- **Flask API**: Backend developed with Flask for seamless data processing and model inference.
- **Interactive Web Interface**: Users can enter symptoms via a user-friendly web interface to get predictions.
- **Responsive Design**: A clean, responsive interface styled with CSS.
- **JSON API Endpoint**: Allows integration with other tools through the `/predict` endpoint.

---

## **Project Structure**

project-folder/ ├── app.py # Flask backend application ├── static/ │ └── style.css # Custom CSS for frontend styling ├── templates/ │ └── index.html # HTML template for the web interface ├── saved_model/ # Saved BERT model and label data │ ├── config.json │ ├── pytorch_model.bin │ ├── tokenizer_config.json │ ├── vocab.txt │ ├── df_label.pkl └── README.md # Project documentation


---

## **Setup and Installation**

### **Prerequisites**

- Python 3.8 or above
- pip (Python package manager)
- A virtual environment (optional but recommended)

### **Steps**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/medical-symptom-detector.git
   cd medical-symptom-detector

2. Set Up a Virtual Environment

   
 
