import streamlit as st
from transformers import pipeline

# Load the pre-trained model from Hugging Face (replace with your model if needed)
@st.cache(allow_output_mutation=True)
def load_translation_model():
    # Load the model pipeline for translation
    model = pipeline("translation_en_to_roman_ur", model="path-to-your-model")
    return model

# Streamlit app
def main():
    st.title("English to Roman Urdu Translation")
    
    # Input from the user
    user_input = st.text_area("Enter an English prompt:", "")
    
    if st.button("Translate"):
        if user_input:
            model = load_translation_model()  # Load the model
            translation = model(user_input)[0]['translation_text']
            st.write(f"Roman Urdu Translation: {translation}")
        else:
            st.write("Please enter an English prompt for translation.")
    
if __name__ == "__main__":
    main()
