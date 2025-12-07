import streamlit as st
import qrcode
import json
import time
from io import BytesIO
from cryptography.fernet import Fernet

st.set_page_config(
    page_title="Encrypted QR Decoder",
    page_icon="🛡️",
    layout="wide"
)



st.markdown("# <span style='color: purple;'>Encrypted QR Generator</span>", unsafe_allow_html=True)
st.markdown("##### Made by Shakib Hossain Tahmid")

# Hidden static key (you can change it once, but keep it secret)
SECRET_KEY = b"w4YNwA3G4gNfCw9xg7tF2z6s2mCzS0TD2Ztq4KSL8gQ="  

fernet = Fernet(SECRET_KEY)

# Inputs
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")


data = {
    "name": name,
    "email": email,
    "phone": phone,

}

if st.button("Generate Encrypted QR"):

    json_data = json.dumps(data)

    encrypted = fernet.encrypt(json_data.encode()).decode()

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(encrypted)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    st.image(img_bytes, caption="Encrypted QR")

    st.download_button(
        "Download QR",
        data=img_bytes,
        file_name="encrypted_qr.png",
        mime="image/png"
    )






st.markdown("> <span style='color: orange;'>*Use sidebar to go to QR Scanner page and Decode it.*</span>", unsafe_allow_html=True)