import streamlit as st
import pandas as pd
import numpy as np


from openai import OpenAI
import os


openai_key = st.secrets['openai_key']

client = OpenAI(api_key = openai_key)

try:
        
    st.session_state.responses_to_avoid

    #st.title('Tinder for Food! Start Swiping!')


    swiping_empty_mechanism = st.empty()
    if st.session_state.counter == 1:
        swiping_empty_mechanism.image(f'{st.session_state.responses_to_avoid}.jpg')



    def reload():
        swiping_empty_mechanism.empty()

        st.session_state.counter = 2
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
                    + f"\n\nONLY ANSWER WITH ONE OF THE RESPONSES ABOVE, NOT A WORD LESS OR MORE. EX: Slice of Pizza = slice-of-pizza\n\nUser Input: {st.session_state.sentence}, don't recommend any of: {st.session_state.responses_to_avoid}"
                )
            }
        ]



        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            max_tokens=40  # Expecting a filename as output
        )

        chatgpt_response = response.choices[0].message.content

        st.image(f'{chatgpt_response}.jpg')

        chatgpt_response = ', ' + chatgpt_response

        with open('responses.txt', 'a') as file:
            file.write(chatgpt_response)

    if 'button' not in st.session_state:
        st.session_state.button = False

    def click_button():
        st.balloons()
        st.session_state.button = not st.session_state.button
        st.session_state.pop('responses_to_avoid')

    columns = st.columns([1, 8, 1])
    with columns[0]:
        st.button('❌', on_click=reload)
    with columns[2]:
        st.button('✅', on_click=click_button)

   
except:

    st.title('Tinder for Food! Start Swiping!')

    empty_mechanism = st.empty()

    sentence  = st.text_area("What're you in the mood for?")

    st.session_state.sentence = sentence

    if st.button('Submit'):
        messages = [
        {"role": "system", "content": "You are an autonomous agent."},
        {
            "role": "user",
            "content": (
                '''Based on the user input, provide a response of food recommendation. \n
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

        chatgpt_response = response.choices[0].message.content

        chatgpt_response = chatgpt_response.replace('Response: ', '')

        #empty_mechanism.image(f'{chatgpt_response}.jpg')

        # Clear the text file and add the chatgpt_response to it
        with open('responses.txt', 'w') as file:
            file.truncate(0)
            file.write(chatgpt_response)

        st.session_state.responses_to_avoid = open('responses.txt').read()
        if sentence:
            empty_mechanism.empty()
            st.session_state.counter = 1
            st.button('start swiping!')

