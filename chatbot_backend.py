import os
import io
import json
import logging
from gtts import gTTS
import speech_recognition as sr
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Setup logging
logging.basicConfig(filename='chatbot_logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Global shared memory
shared_memory = ConversationBufferMemory(max_token_limit=512)

def demo_chatbot(temperature=0.9, top_p=0.5, max_gen_len=512):
    demo_llm = Bedrock(
        credentials_profile_name='default',
        model_id='meta.llama2-13b-chat-v1',
        model_kwargs={
            "temperature": temperature,
            "top_p": top_p,
            "max_gen_len": max_gen_len,
            "stop": ["\nHuman:", "\nAI:"]
        }
    )
    return demo_llm

def demo_memory():
    # Initialize a new, empty memory buffer
    memory = ConversationBufferMemory(max_token_limit=512)
    return memory

def demo_chain(input_text, memory, shared=False, temperature=0.9, top_p=0.5, max_gen_len=512):
    llm_conversation = ConversationChain(
        llm=demo_chatbot(temperature, top_p, max_gen_len),
        memory=shared_memory if shared else memory,
        verbose=True
    )

    # Format the input with INST tags
    formatted_input = f"{input_text} [/INST]"
    chat_reply = llm_conversation.predict(input=formatted_input)

    # Log the interaction
    logging.info(json.dumps({
        "input": input_text,
        "reply": chat_reply,
        "temperature": temperature,
        "top_p": top_p,
        "max_gen_len": max_gen_len
    }))

    return chat_reply

# Speech-to-text function
def speech_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    return text

# Text-to-speech function
def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    audio_file_path = "response.mp3"
    tts.save(audio_file_path)
    return audio_file_path

# Feedback function
def log_feedback(user_feedback):
    logging.info(json.dumps({
        "feedback": user_feedback
    }))
