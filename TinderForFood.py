import streamlit as st
import pandas as pd
import numpy as np

st.title('Tinder for Food! Start Swiping!')

from openai import OpenAI
import os


openai_key = st.secrets["openai"]

client = OpenAI(api_key = openai_key)

if not st.button("Submit"):
    # Get user input
    sentence = st.text_area("what are you hungry for?")


    # Get the list of jpg files in the folder
    folder_path = '/f:/TinderForFood/images'
    jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

    # Create the messages based on the jpg files
    messages = [
        {"role": "system", "content": "You are an autonomous agent."},
        {
            "role": "user",
            "content": (
                '''Based on the user input, give a response that 
                indicates which food they should eat.\n\n'''
                + "\n".join([f"{i+1}. {file.split('.')[0].replace('-', ' ').title()}: Response: {file.split('.')[0]}" for i, file in enumerate(jpg_files)])
                + f"\n\nONLY ANSWER WITH THE RESPONSES ABOVE, NOT A WORD LESS OR MORE.\n\nUser Input: {sentence}"
            )
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        max_tokens=40  # Expecting a single number as output
    )

else:
    st.image(f'{response.choices[0].message.content}.jpg')
    columns = st.columns(3)
    with columns[0]:
        st.button(
            "❌")
    with columns[2]:
        st.button(
            "✅")

    while not st.button( "✅"):
        messages = [
        {"role": "system", "content": "You are an autonomous agent."},
        {
            "role": "user",
            "content": (
                '''Based on the user input, give a response that 
                indicates which food they should eat.\n\n'''
                + "\n".join([f"{i+1}. {file.split('.')[0].replace('_', ' ').title()}: Response: {file.split('.')[0]}" for i, file in enumerate(jpg_files)])
                + f"\n\nONLY ANSWER WITH THE RESPONSES ABOVE, NOT A WORD LESS OR MORE.\n\nUser Input: {sentence}"
            )
        }
        ]

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=40  # Expecting a single number as output
        )

        columns = st.columns(3)
        with columns[0]:
            st.button(
                "❌")
        with columns[2]:
            st.button(
                "✅")