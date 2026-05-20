import streamlit as st
from transformers import pipeline

# Page Title
st.set_page_config(page_title="Cybersecurity Incident Analyzer")

st.title("🔐 GenAI Cybersecurity Incident Analyzer")
st.write("Analyze cybersecurity logs using Chain-of-Thought Prompting")

# Load AI Model
@st.cache_resource
def load_model():
    generator = pipeline(
        "text-generation",
        model="gpt2"
    )
    return generator

generator = load_model()

# User Input
logs = st.text_area(
    "Enter Security Logs",
    height=250,
    placeholder="Paste security logs here..."
)

# Analyze Button
if st.button("Analyze Incident"):

    if logs.strip() == "":
        st.warning("Please enter security logs.")
    else:

        prompt = f"""
You are a cybersecurity analyst.

Analyze the following logs step-by-step.

Tasks:
1. Identify suspicious activities
2. Detect attack pattern
3. Determine severity level
4. Identify affected systems
5. Suggest mitigation strategies
6. Recommend prevention methods

Security Logs:
{logs}

Generate a detailed cybersecurity incident report.
"""

        with st.spinner("Analyzing Incident..."):
            response = generator(
                prompt,
                max_length=400,
                do_sample=True,
                temperature=0.7
            )

        result = response[0]["generated_text"]

        st.subheader("📊 Incident Analysis Report")
        st.write(result)
