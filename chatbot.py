import streamlit as st 
import random
import time

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
  st.session_state.message = []

#Display caht messages from history on app rerun 
for message in st.session state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])


# Accept user input
if prompt := st.chat_input("What is up?"):
  # Display user message in chat message container
  with st.chat_message("user"):
  # Add user message to chat history 
  st.session_state.messages.append({"role": "user", "content": prompt})


# Streamed response emulator
def response_generator():
  response = random.choice(
    [ 
      "Hello there! How can I assist you today?", 
      "Hi human! Is there anything I can help you with?",
      "Hi creator! How can I serve you?",
      "Hi, what can I start for you today?",
      "Do you need help?", 
    ]
  )
  for word in response.split():
    yield word + " " 
    time.sleep(0.05)


# Display assistant response in chat message container
with st.chat message("assistant"):
  response = st.write_stream(response_generator())

# Add assistant response to chat history 
st.session_state.messages.append({"role": "assistant", "content": response})

