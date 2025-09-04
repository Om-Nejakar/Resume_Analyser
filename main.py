import streamlit as st  # for web page
from components import resume, sidebar, chatAi


def show_home():
    st.markdown(
        """
        <style>
        @keyframes borderAnimation {
            0% {border-image-source: linear-gradient(45deg, red, orange);}
            25% {border-image-source: linear-gradient(90deg, orange, yellow);}
            50% {border-image-source: linear-gradient(135deg, yellow, green);}
            75% {border-image-source: linear-gradient(180deg, green, blue);}
            100% {border-image-source: linear-gradient(225deg, blue, red);}
        }

        .animated-border {
            border: 6px solid;
            border-image-slice: 1;
            animation: borderAnimation 5s linear infinite;
            border-radius: 20px;
            padding: 20px;
            font-size: 20px;
            background-color: #111827; /* dark bg */
            box-shadow: 0px 4px 20px rgba(0,0,0,0.5);
            margin-top: 20px;
        }

        .feature-box {
            background-color: #1f2937;
            padding: 20px;
            border-radius: 15px;
            margin: 15px 0;
            color: #e5e7eb;
            text-align: center;
            box-shadow: 0px 3px 12px rgba(0,0,0,0.3);
        }

        .social-icons img {
            width: 45px;
            margin: 8px;
            border-radius: 50%;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .social-icons img:hover {
            transform: scale(1.2);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.4);
        }
        </style>

        <div class="animated-border" style="width: 100%">
            <h2 style='text-align: center; color: white;'>
                Welcome To all in One <span style='color: #1E90FF; text-decoration: underline;'>YouVa-Chat</span> Platform 🚀
            </h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ---- Add gap ----
    st.markdown("<br><br>", unsafe_allow_html=True)

    # ---- Middle Section: Features ----
    st.subheader("What You Can Do Here", divider=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='feature-box'>AI Chat<br><small>Ask anything, anytime</small></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='feature-box'> Resume<br><small>View my profile & skills</small></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='feature-box'> Multi-Mode<br><small>Switch easily between tools</small></div>", unsafe_allow_html=True)

    # ---- Add bigger gap ----
    st.markdown("<br><br><br>", unsafe_allow_html=True)

    # ---- Footer Section: Social Links ----
    st.header("Connect with me: ", divider=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="social-icons">
            <a href="https://github.com/Om-Nejakar" target="_blank">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png">
            </a>
            <a href="https://www.linkedin.com/in/om-nejakar/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )


# Sidebar
with st.sidebar:
    model_choice, start_chat, mode = sidebar.sidebar_ui()

# Routing
if mode == "home":
    show_home()

elif mode == "chat":
    chatAi.chatAi_ui(model_choice, start_chat)

elif mode == "resume":
    resume.resume_ui()

else:
    show_home()
