# 🧠 SWYNEX Intelligent Sentiment Analyzer

An improved AI sentiment analysis prototype developed as part of the SWYNEX Internship Task 3: Intelligent Feature.

## 🚀 Project Overview

This project improves a basic sentiment analysis prototype by adding intelligent features for confidence analysis, evaluation testing, and failure-case detection.

The application uses a pre-trained Transformer model to classify text as Positive or Negative.

## ✨ Intelligent Features

- 🤖 AI-based sentiment prediction
- 📊 Confidence score for every prediction
- 🧠 Confidence-based reliability analysis
- ⚠️ Input validation and edge-case handling
- 🧪 Built-in model evaluation examples
- 🔎 Failure and limitation analysis
- 🌐 Simple Streamlit web interface

## 🛠️ Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Streamlit

## 🧠 Model

The project uses:

distilbert-base-uncased-finetuned-sst-2-english

This is a pre-trained DistilBERT model fine-tuned for sentiment classification.

## 🧪 Evaluation Examples

The application includes predefined examples to demonstrate how the model behaves on different types of text.

Examples include:

- "I absolutely loved this product!"
- "This is the worst experience I have ever had."
- "The movie was okay, nothing special."
- "I expected better from this service."
- "Amazing quality and excellent customer support!"

The application displays the predicted sentiment and confidence score for each example.

## ⚠️ Failure and Edge Cases

The project also evaluates cases where sentiment models may struggle.

### 1. Ambiguous Text

*Input:*

Okay

*Model prediction:* Positive

*Confidence:* 99.98%

"Okay" is ambiguous and does not necessarily express strong positive sentiment.

### 2. Sarcasm

*Input:*

Yeah right...

*Model prediction:* Positive

*Confidence:* 99.85%

The phrase may be sarcastic depending on context, which can be difficult for sentiment models to understand.

### 3. Slang

*Input:*

The product is sick!

*Model prediction:* Negative

*Confidence:* 99.98%

In modern informal language, "sick" can mean something is excellent. The model may interpret the word using its more common negative meaning.

## 💡 Key Learning

This project demonstrates that a high confidence score does not always mean that an AI prediction is correct.

Context, sarcasm, ambiguity, and slang can cause sentiment models to produce incorrect predictions with high confidence.

Therefore, AI predictions should be interpreted carefully rather than treated as absolute truth.

## ▶️ How to Run

### 1. Create and activate a Python environment

```bash
py -3.11 -m venv swynex_env

Windows PowerShell:

.\swynex_env\Scripts\Activate.ps1

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python -m streamlit run app.py

The application will open in your browser.

📁 Project Structure

SWYNEX-Intelligent-Feature/
│
├── app.py
├── README.md
├── requirements.txt
└── swynex_env/

🎯 Internship Task

SWYNEX Internship — Task 3: Intelligent Feature

The project demonstrates:

• Intelligent feature improvement
• Model evaluation examples
• Failure and error cases
• Simple interactive interface
