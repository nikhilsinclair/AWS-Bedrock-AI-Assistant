import streamlit as st
import chatbot_backend as demo

# Custom CSS for styling
st.markdown(
    """
    <style>
    .header {
        font-size: 2em;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 1.2em;
        color: #555;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subheader
st.markdown("<div class='header'>Hi, This is your personal Chatbot 😎</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Chat with your personal chatbot supported by AWS Bedrock right here</div>", unsafe_allow_html=True)

# Sidebar for settings
st.sidebar.title("Chatbot Settings")
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.9)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.5)
max_gen_len = st.sidebar.slider("Max Generation Length", 100, 1000, 512)
share_data = st.sidebar.checkbox("Share data across chats", value=False)

# Initialize the memory buffers and chat history if not already done
if 'memory_buffers' not in st.session_state:
    st.session_state.memory_buffers = {}

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = {}

# Function to handle chat history
def add_to_chat_history(session_id, role, text):
    if session_id not in st.session_state.chat_history:
        st.session_state.chat_history[session_id] = []
    st.session_state.chat_history[session_id].append({"role": role, "text": text})

# Sidebar for session management
st.sidebar.title("Chat Sessions")
session_names = list(st.session_state.chat_history.keys())
current_session = st.sidebar.selectbox("Select Session", options=session_names + ["New Session"])
if current_session == "New Session":
    new_session_name = st.sidebar.text_input("Enter new session name")
    if st.sidebar.button("Create Session"):
        current_session = new_session_name
        st.session_state.chat_history[current_session] = []
        if not share_data:
            st.session_state.memory_buffers[current_session] = demo.demo_memory()

# Delete session functionality
if current_session in session_names:
    if st.sidebar.button("Delete Session"):
        del st.session_state.chat_history[current_session]
        if not share_data and current_session in st.session_state.memory_buffers:
            del st.session_state.memory_buffers[current_session]
        current_session = session_names[0] if session_names else "New Session"

# Display chat history for the current session
if current_session in st.session_state.chat_history:
    for message in st.session_state.chat_history[current_session]:
        with st.chat_message(message["role"]):
            if message["role"] == "user":
                st.markdown(f"<div class='chat-bubble user-bubble'>{message['text']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='chat-bubble assistant-bubble'>{message['text']}</div>", unsafe_allow_html=True)

# User input options
st.markdown("### Enter your message")
input_text = st.chat_input("Type your message here...")

uploaded_audio = st.file_uploader("Or upload an audio file", type=["wav", "mp3"])

# Feedback mechanism
st.markdown("### Provide Feedback")
feedback = st.text_area("Feedback about the bot's response")

if st.button("Submit Feedback"):
    demo.log_feedback(feedback)
    st.success("Feedback submitted!")

if input_text:
    # Display user message
    with st.chat_message("user"):
        st.markdown(f"<div class='chat-bubble user-bubble'>{input_text}</div>", unsafe_allow_html=True)
    add_to_chat_history(current_session, "user", input_text)

    # Determine which memory buffer to use
    if share_data:
        memory = demo.shared_memory
    else:
        if current_session not in st.session_state.memory_buffers:
            st.session_state.memory_buffers[current_session] = demo.demo_memory()
        memory = st.session_state.memory_buffers[current_session]

    # Get chatbot response
    chat_response = demo.demo_chain(
        input_text=input_text, 
        memory=memory,
        shared=share_data,
        temperature=temperature,
        top_p=top_p,
        max_gen_len=max_gen_len
    )
