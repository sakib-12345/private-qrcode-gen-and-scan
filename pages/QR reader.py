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
                t = "Empty" if obj['msg'] == "" else obj['msg'].replace("_", " ")
                c = "red" if obj['msg'] == "" else "green"
                st.markdown("> Message")
                st.markdown(f"<span style='color: {c};'>{t}</span>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Decrypt failed: {e}")

st.markdown("> <span style='color: orange;'>Scanner synced with generator ✅</span>", unsafe_allow_html=True)


st.sidebar.markdown(
    """
    <style>
        .social-icons {
            text-align: center;
            margin-top: 40px;
        }

        .social-icons a {
            text-decoration: none !important;
            margin: 0 10px;
            font-size: 20px;
            display: inline-block;
            color: inherit !important; /* force child i to use its color */
        }

        

        /* Hover glitch animation */
        .social-icons a:hover {
            animation: glitch 0.3s infinite;
        }

        
        /* Contact us heading */
        .contact-heading {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 15px;
        }
        @keyframes glitch {
            0% { transform: translate(0px, 0px); text-shadow: 2px 2px #0ff, -2px -2px #f0f; }
            20% { transform: translate(-2px, 1px); text-shadow: -2px 2px #0ff, 2px -2px #f0f; }
            40% { transform: translate(2px, -1px); text-shadow: 2px -2px #0ff, -2px 2px #f0f; }
            60% { transform: translate(-1px, 2px); text-shadow: -2px 2px #0ff, 2px -2px #f0f; }
            80% { transform: translate(1px, -2px); text-shadow: 2px -2px #0ff, -2px 2px #f0f; }
            100% { transform: translate(0px, 0px); text-shadow: 2px 2px #0ff, -2px -2px #f0f; }
        }
    </style>
    <div class="social-icons">
    <div class="contact-heading">Contact Us:</div>
        <a class='fb' href='https://www.facebook.com/sakibhossain.tahmid' target='_blank'>
            <i class='fab fa-facebook'></i> 
        </a> 
        <a class='insta' href='https://www.instagram.com/_sakib_000001' target='_blank'>
            <i class='fab fa-instagram'></i> 
        </a> 
        <a class='github' href='https://github.com/sakib-12345' target='_blank'>
            <i class='fab fa-github'></i> 
        </a> 
        <a class='email' href='mailto:sakibhossaintahmid@gmail.com'>
            <i class='fas fa-envelope'></i> 
        </a>
    </div>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """,
    unsafe_allow_html=True
)


st.markdown(
            f'<div style="text-align: center; color: grey;">&copy; 2025 Sakib Hossain Tahmid. All Rights Reserved.</div>',
            unsafe_allow_html=True

           ) 

