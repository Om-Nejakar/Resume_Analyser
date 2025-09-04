
import streamlit as st # for web page
from components import resume, sidebar, chatAi

with st.sidebar:
    model_choice, start_chat, mode= sidebar.sidebar_ui()

if mode == "home":
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
            border-width: 6px;
            animation: borderAnimation 4s linear infinite;
            border-radius: 20px;
            padding: 10px;
            font-size: 18px;
        }
        </style>

        <div class="animated-border" style="width: 100%">
            <h2 style='text-align: center;'>Welcome To all in One <span style='color: #1E90FF; text-decoration: underline;'>YouVa-Chat</span> Platform</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    # st.image("https://cdn.pixabay.com/photo/2024/05/16/19/29/ai-generated-8766874_960_720.jpg")
    st.header(":red[Connect with me: ]", divider=True)

    st.markdown(
        """
        <a href="https://github.com/Om-Nejakar" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" style="border-radius:50%">
        </a>
        <a href="https://www.linkedin.com/in/om-nejakar/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="35" style="margin-left:10px;border-radius:50%;">
        </a>
        """,
        unsafe_allow_html=True
    )
    

elif  mode == "chat":
    chatAi.chatAi_ui(model_choice, start_chat)

elif mode == "resume":
    resume.resume_ui()
else:
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
            border-width: 6px;
            animation: borderAnimation 4s linear infinite;
            border-radius: 20px;
            padding: 10px;
            font-size: 18px;
        }
        </style>

        <div class="animated-border" style="width: 100%">
            <h2 style='text-align: center;'>Welcome To all in One <span style='color: #1E90FF; text-decoration: underline;'>YouVa-Chat</span> Platform</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    # st.image("https://cdn.pixabay.com/photo/2024/05/16/19/29/ai-generated-8766874_960_720.jpg")
    st.header(":red[Connect with me:]", divider=True)
    st.markdown(
        """
        <a href="https://github.com/Om-Nejakar" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="40" style="border-radius:50%">
        </a>
        <a href="https://www.linkedin.com/in/om-nejakar/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="35" style="margin-left:10px;border-radius:50%;">
        </a>
        """,
        unsafe_allow_html=True
    )
    