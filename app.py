from io import BytesIO

import streamlit as st
from PIL import Image
from rembg import new_session, remove

st.title("Remove Background!")

# Upload the file
image_upload = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])


# Convert the image to BytesIO so we can download it!
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


# If we've uploaded an image, open it and remove the background!
if image_upload:
    # SHOW the uploaded image!
    st.image(image_upload)
    image = Image.open(image_upload)
    model_name = "isnet-general-use"
    session = new_session(model_name)
    fixed = remove(image, session=session)
    downloadable_image = convert_image(fixed)
    # SHOW the improved image!
    st.image(downloadable_image)
    st.download_button(
        "Download fixed image", downloadable_image, "fixed.png", "image/png"
    )
