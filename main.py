
import streamlit as st # for web page
from components import resume, sidebar, chatAi


with st.sidebar:
    model_choice, start_chat, mode= sidebar.sidebar_ui()

if mode == "home":
    st.markdown(
    "<h2 style='text-align: center;'>Welcome To all in One <span style='color: #1E90FF; text-decoration: underline;'>YouVa-Chat</span> Platform</h2>",
    unsafe_allow_html=True
    )
    st.image("https://cdn.pixabay.com/photo/2024/05/16/19/29/ai-generated-8766874_960_720.jpg")
    st.header(":red[Connect with me: ]", divider=True)
elif  mode == "chat":
    chatAi.chatAi_ui(model_choice, start_chat)

elif mode == "resume":
    resume.resume_ui()
else:
    st.markdown(
    "<h2 style='text-align: center;'>Welcome To all in One <span style='color: #1E90FF; text-decoration: underline;'>YouVa-Chat</span> Platform</h2>",
    unsafe_allow_html=True
    )
    st.image("https://cdn.pixabay.com/photo/2024/05/16/19/29/ai-generated-8766874_960_720.jpg")
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
    