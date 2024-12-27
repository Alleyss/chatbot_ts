import streamlit as st
from api_client import get_streaming_chat_response
from utils import load_sections, save_sections, add_new_section, get_section_conversation, add_message_to_section

st.title("Grok-Powered Chatbot for Streamlit")

# Load existing sections
sections = load_sections()

# Initialize session state
if "selected_section" not in st.session_state:
    st.session_state.selected_section = None

# Sidebar for Section Management
with st.sidebar:
    st.header("Sections")
    new_section_title = st.text_input("New Section Title")
    if st.button("Create New Section"):
        if new_section_title:
            sections = add_new_section(sections, new_section_title)
            st.session_state.selected_section = new_section_title
            st.rerun()

    # Display the section buttons (menu)
    if sections:
        for section_title in sections:
            if st.button(section_title, key=section_title):
                st.session_state.selected_section = section_title
                st.rerun()

# Main content area for displaying conversation
if st.session_state.selected_section:
    st.header(f"Section: {st.session_state.selected_section}")
    conversation = get_section_conversation(sections, st.session_state.selected_section)
    for message in conversation:
      with st.chat_message(message["role"]):
        st.markdown(message["content"])

    if prompt := st.chat_input("Ask me about Streamlit"):
        # Get last 5 conversation turns
        last_5_messages = conversation[-5:]
        message_user = {"role": "user", "content": prompt}
        sections = add_message_to_section(sections, st.session_state.selected_section, message_user)
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Call the get_streaming_chat_response function with user input
             response_stream = get_streaming_chat_response(prompt, last_5_messages,0.5,0.9)
            # Use a generator to enable streaming
             response = st.write_stream(response_stream)
        message_assistant = {"role": "assistant", "content": response}
        sections = add_message_to_section(sections, st.session_state.selected_section, message_assistant)