import streamlit as st 

st.set_page_config(page_title='chat with me ')
st.write(
    """
    Welcome to the chatbot interface! Type your message below to interact with me.
    """
)

user_message = st.text_input('Your message')

if user_message:
    response = 'Chatbot:'+ user_message
    st.write(response
"""
)