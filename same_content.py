import streamlit as st

def side_note():
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
        </style>
        
        <div class="about-title-dark">About This Page</div>

        <div class="about-box-dark">
            This page handles encrypted QR codes only.<br><br>
            Other scanners won't work because the QR payload is encrypted.<br><br>
            Built for secure generation and scanning without data leaks.
        </div>

        """,
        unsafe_allow_html=True
    )

def social_links():
    
    st.markdown(
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
            '<div style="text-align: center; color: grey;">v1.0.0</div>',
            unsafe_allow_html=True

           ) 

def header():
    
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

