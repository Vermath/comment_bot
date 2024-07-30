import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]
client = OpenAI(api_key=openai_api_key)


def ask_gpt4o_mini(question):
    response = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:market-research-gpt:tessa-test:9qSE52j7",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def main():
    st.title("GPT-4o Mini Q&A")

    # User input
    user_question = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        if user_question:
            with st.spinner("Generating answer... This may take a while."):
                try:
                    answer = ask_gpt4o_mini(user_question)
                    st.write("Answer:", answer)
                except Exception as e:
                    st.error(f"Error generating answer: {str(e)}")
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()