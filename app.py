import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="SWYNEX Intelligent Sentiment Analyzer",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Intelligent Sentiment Analyzer")
st.write(
    "An improved sentiment analysis prototype with confidence analysis, "
    "failure detection, and evaluation examples."
)

# Load the sentiment model
@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

classifier = load_model()

# Input section
st.subheader("🔍 Analyze Text")

text = st.text_area(
    "Enter a sentence:",
    placeholder="Example: I really enjoyed this product!"
)

if st.button("Analyze Sentiment"):
    if not text.strip():
        st.warning("⚠️ Please enter some text before analyzing.")
    elif len(text.strip()) < 3:
        st.warning("⚠️ The input is too short to analyze reliably.")
    else:
        result = classifier(text)[0]

        label = result["label"]
        confidence = result["score"]
        confidence_percent = confidence * 100

        # Display sentiment
        if label == "POSITIVE":
            st.success(f"😊 Sentiment: {label}")
        else:
            st.error(f"😞 Sentiment: {label}")

        st.metric(
            "Confidence",
            f"{confidence_percent:.2f}%"
        )

        # Intelligent confidence analysis
        st.subheader("🧠 Intelligent Analysis")

        if confidence_percent >= 80:
            st.success(
                "High confidence: the model is relatively confident "
                "about this prediction."
            )
        elif confidence_percent >= 60:
            st.warning(
                "Medium confidence: the prediction should be interpreted "
                "with some caution."
            )
        else:
            st.error(
                "Low confidence: this input may be ambiguous, unusual, "
                "or difficult for the model to classify."
            )

        # Basic failure-case detection
        if len(text.split()) <= 2:
            st.info(
                "⚠️ Possible failure case: very short inputs can provide "
                "insufficient context."
            )

        if "not" in text.lower() or "never" in text.lower():
            st.info(
                "🔎 Note: negation words such as 'not' or 'never' can "
                "make sentiment interpretation more difficult."
            )


# Evaluation examples
st.divider()
st.subheader("🧪 Model Evaluation Examples")

evaluation_examples = [
    "I absolutely loved this product!",
    "This is the worst experience I have ever had.",
    "The movie was okay, nothing special.",
    "I expected better from this service.",
    "Amazing quality and excellent customer support!"
]

if st.button("Run Evaluation Examples"):
    for example in evaluation_examples:
        result = classifier(example)[0]

        label = result["label"]
        confidence = result["score"] * 100

        st.write(f"*Input:* {example}")
        st.write(
            f"Prediction: *{label}* | "
            f"Confidence: *{confidence:.2f}%*"
        )
        st.write("---")


# Failure cases
st.divider()
st.subheader("⚠️ Failure / Edge Cases")

failure_cases = [
    "",
    "Okay",
    "Not bad",
    "Yeah right...",
    "The product is sick!"
]

for case in failure_cases:
    if case == "":
        display_text = "(empty input)"
    else:
        display_text = case

    st.write(f"• {display_text}")

st.caption(
    "Note: AI predictions are probabilistic and may be incorrect, "
    "especially for sarcasm, slang, short inputs, or ambiguous language."
)