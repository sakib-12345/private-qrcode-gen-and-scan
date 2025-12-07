import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import cv2
from cryptography.fernet import Fernet
import json


st.set_page_config(
    page_title="Encrypted QR Decoder",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("# <span style='color: purple;'>Encrypted QR Decoder</span>", unsafe_allow_html=True)
# -----------------------------
# Hidden secret key (same as generator)
# -----------------------------
SECRET_KEY = b"w4YNwA3G4gNfCw9xg7tF2z6s2mCzS0TD2Ztq4KSL8gQ="  
fernet = Fernet(SECRET_KEY)


mode = st.radio("Choose scanner:", ["Upload Image", "Camera Scan"])

encrypted_text = None

# ---------------------------------------------------
# MODE 1: Upload Image Scanner
# ---------------------------------------------------
if mode == "Upload Image":

    uploaded = st.file_uploader("Upload Encrypted QR", type=["png", "jpg", "jpeg"])

    if uploaded:
        img = Image.open(uploaded).convert("RGB")

        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        decoded = decode(gray)

        if decoded:
            encrypted_text = decoded[0].data.decode()
            

        else:
            detector = cv2.QRCodeDetector()
            text, _, _ = detector.detectAndDecode(gray)

            if text:
                encrypted_text = text
            else:
                st.error("No QR found")

# ---------------------------------------------------
# MODE 2: Camera Scanner
# ---------------------------------------------------
elif mode == "Camera Scan":

    st.write("Scan using your webcam")

    frame = st.camera_input("Camera")

    if frame:
        img = Image.open(frame).convert("RGB")
        

        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        decoded = decode(gray)

        if decoded:
            encrypted_text = decoded[0].data.decode()
            st.success("Encrypted QR extracted")

        else:
            detector = cv2.QRCodeDetector()
            text, _, _ = detector.detectAndDecode(gray)

            if text:
                encrypted_text = text
                st.success("Encrypted QR extracted")

# ---------------------------------------------------
# DECRYPT BUTTON
# ---------------------------------------------------

if st.button("Decrypt"):

    if not encrypted_text:
        st.error("Scan or upload a QR first.")

    else:
        try:
            decrypted = fernet.decrypt(encrypted_text.encode()).decode()

            obj = json.loads(decrypted)
            Name = obj["name"]
            Email = obj["email"]
            Phone = obj["phone"]
            with st.expander("Information", expanded=True):
                st.markdown("> Name:")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: orange;'>{Name}</span>", unsafe_allow_html=True)
                st.markdown("> Email:")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: orange;'>{Email}</span>", unsafe_allow_html=True)
                st.markdown("> Phone:")
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style='color: orange;'>{Phone}</span>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Decryption failed: {e}")
