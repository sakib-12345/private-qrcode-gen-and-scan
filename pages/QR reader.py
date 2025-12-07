import streamlit as st
from PIL import Image
import numpy as np
import cv2
from cryptography.fernet import Fernet
import json

st.set_page_config(
    page_title="Encrypted QR Scanner",
    page_icon="🛡️",
    layout="wide",
)

st.markdown("# <span style='color: purple;'>Encrypted QR Scanner</span>", unsafe_allow_html=True)
st.markdown("##### Made by Shakib Hossain Tahmid")

SECRET_KEY = b"w4YNwA3G4gNfCw9xg7tF2z6s2mCzS0TD2Ztq4KSL8gQ="
fernet = Fernet(SECRET_KEY)

mode = st.radio("Mode:", ["Upload Image", "Camera Scan"])

encrypted_text = None

def detect_qr(gray):
    detector = cv2.QRCodeDetector()
    text, _, _ = detector.detectAndDecode(gray)
    return text

# -----------------------------
# Upload Mode
# -----------------------------
if mode == "Upload Image":
    uploaded = st.file_uploader("Upload Encrypted QR", type=["png", "jpg", "jpeg"])

    if uploaded:
        img = Image.open(uploaded).convert("RGB")

        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        text = detect_qr(gray)

        if text:
            encrypted_text = text
            st.success("QR detected ✅")
        else:
            st.error("No QR found")


# -----------------------------
# Camera Mode
# -----------------------------
elif mode == "Camera Scan":

    frame = st.camera_input("Camera")

    if frame:
        img = Image.open(frame).convert("RGB")

        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

        text = detect_qr(gray)

        if text:
            encrypted_text = text
            st.success("QR extracted ✅")
        else:
            st.warning("No QR detected")


# -----------------------------
# Decrypt Button
# -----------------------------
if st.button("Decrypt QR"):

    if not encrypted_text:
        st.error("Scan or upload a QR first.")
    else:
        try:
            decrypted = fernet.decrypt(encrypted_text.encode()).decode()
            obj = json.loads(decrypted)

            with st.expander("Decoded Information", expanded=True):

                st.markdown("> Name:")
                st.markdown(f"<span style='color: orange;'>{obj['name']}</span>", unsafe_allow_html=True)

                st.markdown("> Email:")
                st.markdown(f"<span style='color: orange;'>{obj['email']}</span>", unsafe_allow_html=True)

                st.markdown("> Phone:")
                st.markdown(f"<span style='color: orange;'>{obj['phone']}</span>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Decrypt failed: {e}")

st.markdown("> <span style='color: orange;'>Scanner synced with generator ✅</span>", unsafe_allow_html=True)
