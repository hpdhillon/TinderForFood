import streamlit as st
import pandas as pd
import numpy as np

st.title('Tinder for Food! Start Swiping!')

from openai import OpenAI

openai_key = st.secrets["openai"]

client = OpenAI(api_key = openai_key)

# Get user input
sentence = st.text_area("what are you hungry for?")


response = client.chat.completions.create(
                model="gpt-4o",  # Specify the model you wish to use
                messages=[
                    {"role": "system", "content": "You are an autonomous agent."},
                    {
                        "role": "user",
                        "content": (
                            '''Based on the user input, give a response that 
                            indicates which food they should eat.

                            1. A Slice of Pizza: Response: slice_of_pizza"
                            2. Grilled Chicken Sandwich: Response: grilled_chicken_sandwich
                            3. Cheeseburger: Response: cheeseburger

                            ONLY ANSWER WITH THE RESPONSES ABOVE, NOT A WORD LESS OR MORE
                            .\n\n'''
                            f"User Input: {sentence}"
                        )
                    }
                ],
                max_tokens=40  # Expecting a single number as output
)

st.write(response.choices[0].message.content)

st.image(f"https://source.unsplash.com/featured/?{response.choices[0].message.content}", use_column_width=True)

