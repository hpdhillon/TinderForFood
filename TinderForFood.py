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


st.session_state.responses_to_avoid = ''
if not st.session_state.responses_to_avoid:
    chatgpt_response = ''


if sentence:
    messages = [
        {"role": "system", "content": "You are an autonomous agent."},
        {
            "role": "user",
            "content": (
                '''Based on the user input, give a response that 
                indicates which food they should eat. \n
                1. Slice of Pizza: Response: slice-of-pizza\n
                2. Cheeseburger: Response: cheeseburger\n
                3. French Fries, Response: french-fries\n
                4. Grilled Chicken Sandwich, Response: grilled-chicken-sandwich\n
                5. BBQ Ribs, Response: bbq-ribs\n
                6. Hot Dog, Response: hot-dog\n
                7. Steak, Response: steak\n
                '''
                + f"\n\nONLY ANSWER WITH ONE OF THE RESPONSES ABOVE, NOT A WORD LESS OR MORE.\n\nUser Input: {sentence}"
            )
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        max_tokens=40  # Expecting a single number as output
    )

    st.write(chatgpt_response)

    if chatgpt_response=='':
        empty_mechanism = st.empty()

        chatgpt_response = response.choices[0].message.content

        chatgpt_response = chatgpt_response.replace('Response: ', '')

        empty_mechanism.image(f'{chatgpt_response}.jpg')

        # Clear the text file and add the chatgpt_response to it
        with open('responses.txt', 'w') as file:
            file.truncate(0)
            file.write(chatgpt_response)

        st.write("stuck_here")


    def reload():
        empty_mechanism.empty()

        st.session_state.responses_to_avoid = open('responses.txt').read()

        messages = [
            {"role": "system", "content": "You are an autonomous agent."},
            {
                "role": "user",
                "content": (
                    '''Based on the user input, give a response that 
                    indicates which food they should eat. \n
                    1. Slice of Pizza: Response: slice-of-pizza\n
                    2. Cheeseburger: Response: cheeseburger\n
                    3. French Fries, Response: french-fries\n
                    4. Grilled Chicken Sandwich, Response: grilled-chicken-sandwich\n
                    5. BBQ Ribs, Response: bbq-ribs\n
                    6. Hot Dog, Response: hot-dog\n
                    7. Steak, Response: steak\n
                    '''
                    + f"\n\nONLY ANSWER WITH ONE OF THE RESPONSES ABOVE, NOT A WORD LESS OR MORE. EX: Slice of Pizza = slice-of-pizza\n\nUser Input: {sentence}, don't recommend any of: {st.session_state.responses_to_avoid}, take that into account"
                )
            }
        ]

        st.write(f"\n\nONLY ANSWER WITH ONE OF THE RESPONSES ABOVE, NOT A WORD LESS OR MORE. EX: Slice of Pizza = slice-of-pizza\n\nUser Input: {sentence}, don't recommend any of: {st.session_state.responses_to_avoid}, take that into account")


        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=40  # Expecting a filename as output
        )

        chatgpt_response = response.choices[0].message.content

        st.write(chatgpt_response)

        st.image(f'{chatgpt_response}.jpg')

        chatgpt_response = ', ' + chatgpt_response

        with open('responses.txt', 'w') as file:
            file.write(chatgpt_response)

        st.write(st.session_state.responses_to_avoid)


    if 'button' not in st.session_state:
        st.session_state.button = False

    def click_button():
        st.session_state.button = not st.session_state.button

    st.columns(2)
    st.button('✅', on_click=click_button)

    st.button('❌', on_click=reload)
