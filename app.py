# Importing the libraries
import streamlit as st 
from prompt_engine import run_prompt

# Creating a Streamlit Page
st.set_page_config(page_title="Prompt Engineering App", layout="centered")
st.title("Prompt Engineering App")

# Prompt Types Dropdown
prompt_types = [
    "Zero-shot",
    "Few-shot",
    "Instruction-based",
    "Chain-of-Thought",
    "Role-Based"
]

selected_prompt = st.selectbox("Choose Prompt Type :", prompt_types)
user_input = st.text_area("Enter your Prompt over here :", height=150)

if st.button("Generate the Content"):
    with st.spinner("Generating Content..."):
        output = run_prompt(selected_prompt, user_input)
        st.markdown("Response:")
        st.code(output)
