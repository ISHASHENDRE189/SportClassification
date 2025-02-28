import streamlit as st
from tensorflow.keras.models import load_model
from utils import predict_label
from PIL import Image

from transformers import pipeline
import numpy as np
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from huggingface_hub import from_pretrained_keras

st.title("Sports Image Classification")

st.write("Predict the sport that is being represented in the image.")

#model = load_model("my_model.keras")
model = from_pretrained_keras('isharani/sportClassification')
#extractor = AutoFeatureExtractor.from_pretrained("yangy50/garbage-classification")
#model = AutoModelForImageClassification.from_pretrained("yangy50/garbage-classification")
#extractor = AutoFeatureExtractor.from_pretrained("keras-io/Image-Classification-using-EANet")
#model = AutoModelForImageClassification.from_pretrained("keras-io/Image-Classification-using-EANet")

with st.form("my_form"):
    uploaded_file = st.file_uploader(
        "Upload an image of a sport being played:", type="jpg"
    )
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        label = predict_label(image, model)

    submitted = st.form_submit_button("Submit")
    if submitted:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.markdown(
                f"<h2 style='text-align: center;'>{label}</h2>",
                unsafe_allow_html=True,
            )
        else:
            st.write("Please upload file or choose sample image.")


st.write(
    "If you would not like to upload an image, you can use the sample image instead:"
)
sample_img_choice = st.button("Use Sample Image")

if sample_img_choice:
    image = Image.open("test_cricket.jpg")
    st.image(image, caption="Image", use_column_width=True)
    label = predict_label(image, model)
    st.markdown(
        f"<h2 style='text-align: center;'>{label}</h2>",
        unsafe_allow_html=True,
    )
