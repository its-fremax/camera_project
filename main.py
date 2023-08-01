import streamlit as st
from PIL import Image

with st.expander("Start camera"):
    camera = st.camera_input("Camera")

if camera:
    img = Image.open(camera)
    grey_img = img.convert("L")
    st.image(grey_img)

upload_image = st.file_uploader("upload image")

if upload_image:
    images = Image.open(upload_image)
    grey_ = images.convert("L")
    st.image(grey_)
