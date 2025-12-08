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
    placeholder="Start typing...",
    label_visibility="visible"
)
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

















