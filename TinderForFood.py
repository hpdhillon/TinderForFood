import streamlit as st
import pandas as pd
import numpy as np

st.title('Tinder for Food! Start Swiping!')

from openai import OpenAI
import os


openai_key = st.secrets["openai"]

client = OpenAI(api_key = openai_key)

# Get user input
sentence = st.text_area("what are you hungry for?")
# Create the messages based on the jpg files
messages = [
    {"role": "system", "content": "You are an autonomous agent."},
    {
        "role": "user",
        "content": (
            '''Based on the user input, give a response that 
            indicates which food they should eat. \n
            1. Slice of Pizza: Response: slice-of-pizza\n
            2. Burger: Response: burger\n
            3. French Fries, Response: french-fries\n
            4. Grilled Chicken Sandwich, Response: grilled-chicken-sandwich\n
            5. BBQ Ribs, Response: bbq-ribs\n
            6. Hot Dog, Response: hot-dog\n
            7. Steak, Response: steak\n
            '''
            + f"\n\nONLY ANSWER WITH THE RESPONSES ABOVE, NOT A WORD LESS OR MORE.\n\nUser Input: {sentence}"
        )
    }
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=messages,
    max_tokens=40  # Expecting a single number as output
)
st.image(f'{response.choices[0].message.content}.jpg')
columns = st.columns(3)
with columns[0]:
    st.button(
        "❌")
with columns[2]:
    st.button(
        "✅")

if st.button("❌"):
    while not st.button( "✅"):
        messages = [
        {"role": "system", "content": "You are an autonomous agent."},
        {
            "role": "user",
            "content": (
                '''Based on the user input, give a response that 
                indicates which food they should eat. \n
                1. Slice of Pizza: Response: slice-of-pizza\n
                2. Burger: Response: burger\n
                3. French Fries, Response: french-fries\n
                4. Grilled Chicken Sandwich, Response: grilled-chicken-sandwich\n
                5. BBQ Ribs, Response: bbq-ribs\n
                6. Hot Dog, Response: hot-dog\n
                7. Steak, Response: steak\n
                '''
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