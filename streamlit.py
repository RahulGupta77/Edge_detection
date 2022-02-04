from PIL import Image
import numpy as np
import streamlit as st
from project import * 

st.set_page_config(initial_sidebar_state="expanded")

st.title("Edge detection ")

img_file_buffer = st.file_uploader('Upload a PNG image', type= ['png','jpg','jpeg'])
if img_file_buffer is not None:
    image = Image.open(img_file_buffer)
    img_array = np.array(image)

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Sobel_detector", "Canny_detector", "Sobel Canny Comparision")
)


if add_selectbox == "Sobel_detector":
    st.header("In Sobel_detector")
    st.image(image)
    sobel_img = sobel(img_array)
    st.subheader("Output : ")
    st.image(sobel_img)
    
elif add_selectbox=="Canny_detector": 
    st.header("In Canny_detector")
    st.image(image)
    canny_img = canny(img_array)
    st.subheader("Output : ")
    st.image(canny_img)

else:
    st.header("In Sobel Canny Comparision")
    st.image(image)
    st.subheader("")
    sobel_img = sobel(img_array)
    canny_img = canny(img_array)
    st.subheader("Output : ")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.text("sobel_detector")
        st.image(sobel_img)
        
    with col2:
        st.text("canny_detector")
        st.image(canny_img)
