# Personal Chatbot with AWS Bedrock

## Visual

![Alt Text](visual.png)


## Overview

This project implements a personal chatbot using AWS Bedrock, integrated with Streamlit for the front-end interface. The chatbot supports multi-modal inputs and outputs, including voice interaction, and incorporates features for image and media handling. Additionally, the chatbot includes analytics and insights capabilities to track user interactions and improve responses over time.

## Features

### Multi-modal Inputs and Outputs

The chatbot supports various input and output modes, including text, voice, and media content. Users can interact with the chatbot through different modalities, enhancing the user experience and accessibility.

### Voice Interaction

Integrated speech-to-text and text-to-speech functionalities enable users to interact with the chatbot through voice commands and responses. The chatbot can understand spoken input and respond with spoken audio, creating a more natural and intuitive interaction flow.

### Image and Media Handling

Users can upload images, videos, or other multimedia content as input to the chatbot. The chatbot utilizes image recognition and processing techniques to analyze and respond to media content effectively. For example, users can ask questions about objects in an image, and the chatbot can provide relevant information or responses.

### Analytics and Insights

The chatbot tracks user interactions to analyze user behavior and improve response accuracy. A feedback loop allows users to rate responses and provide comments for further refinement. Additionally, the chatbot generates insights and analytics reports to help developers understand usage patterns and identify areas for improvement.

## Technologies Used

### AWS Bedrock

AWS Bedrock is the core technology powering the chatbot's natural language processing capabilities. Bedrock leverages state-of-the-art language models and machine learning algorithms to understand and generate human-like responses.

### Streamlit

Streamlit is used to create the interactive front-end interface for the chatbot. Streamlit provides a user-friendly experience for interacting with the chatbot, allowing users to input text, voice, and media content seamlessly.

### Google Text-to-Speech (gTTS)

gTTS is utilized for text-to-speech conversion, enabling the chatbot to respond with spoken audio. gTTS provides high-quality, natural-sounding speech synthesis, enhancing the chatbot's voice interaction capabilities.

### Watchdog

Watchdog is a Python library used for monitoring file system events. While initially intended for image handling, it was later removed due to complexity. However, it remains a useful tool for monitoring and managing other aspects of the project's file system.

## How to Run

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run chatbot_frontend.py`.
4. Interact with the chatbot through the provided interface.


