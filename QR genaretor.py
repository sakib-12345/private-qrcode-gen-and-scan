import streamlit as st
import qrcode
import json
from io import BytesIO
from cryptography.fernet import Fernet

st.set_page_config(
    page_title="Encrypted QR Generator",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("# <span style='color: purple;'>Encrypted QR Generator</span>", unsafe_allow_html=True)
st.markdown("##### Made by Shakib Hossain Tahmid")

# Static secret key
SECRET_KEY = b"w4YNwA3G4gNfCw9xg7tF2z6s2mCzS0TD2Ztq4KSL8gQ="
fernet = Fernet(SECRET_KEY)

def num_check(number):
    if int(number) > 999999999 and int(number) < 10000000000:
        return True
    else:
        return False

name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
text = st.text_area(
    "Message (Optional):",
    height=150,  # Set the height in pixels
    placeholder="complex text won't work.....",
    label_visibility="visible"
)
if text:
    text = text.strip().replace("\n", "").replace(" ", "_")
click = st.button("Generate Encrypted QR")

data = {
    "name": name,
    "email": email,
    "phone": phone,
    "msg": text
}

if click:
    try:
        valid_num = num_check(phone)
    except Exception:
        valid_num = False
    if valid_num:    
        if name and email and phone:
            json_data = json.dumps(data)

            encrypted = fernet.encrypt(json_data.encode()).decode()

    # ✅ Bigger QR → scans easily
            qr = qrcode.QRCode(
            version=4,
            box_size=12,
            border=4
             )

            qr.add_data(encrypted)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

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

        else:
            st.error("Please Fill Name and Email")

    else:
        st.error("The phone number is invalid or empty")
        st.markdown("""
        - The number must be **11-digit** and **Integer**.
        - It must be starts with **"01"** like **01XXXXXXXXX**
        """)

st.markdown("> <span style='color: orange;'>Use the scanner page to decode it.</span>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        """
        <style>
        .about-title-dark {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 12px;
            color: #c084fc;
        }

        .about-box-dark {
            padding: 14px 16px;
            background: #1e1e2e;
            border-left: 4px solid #a855f7;
            border-radius: 10px;
            font-size: 14px;
            line-height: 1.6;
            color: #e9d5ff;
            box-shadow: 0 0 8px rgba(168, 85, 247, 0.15);
        }

        .about-footer {
            margin-top: 18px;
            font-size: 12px;
            color: #a78bfa;
        }
        </style>
        
        <div class="about-title-dark">About This Page</div>

        <div class="about-box-dark">
            This page handles encrypted QR codes only.<br><br>
            Other scanners won't work because the QR payload is encrypted.<br><br>
            Built for secure generation and scanning without data leaks.
        </div>

        <p class="about-footer">v1.0 • by Sakib</p>
        """,
        unsafe_allow_html=True
    )



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




















