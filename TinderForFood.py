import streamlit as st
import pandas as pd
import numpy as np

st.title('Tinder for Food! Start Swiping!')

from openai import OpenAI


from streamlit_carousel import carousel

openai_key = st.secrets["openai"]

client = OpenAI(api_key = openai_key)

if not st.button("Submit"):
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

elif st.button("Submit"):

    test_items = [
        dict(
            title="Slide 1",
            text="A tree in the savannah",
            img="https://img.freepik.com/free-photo/wide-angle-shot-single-tree-growing-clouded-sky-during-sunset-surrounded-by-grass_181624-22807.jpg?w=1380&t=st=1688825493~exp=1688826093~hmac=cb486d2646b48acbd5a49a32b02bda8330ad7f8a0d53880ce2da471a45ad08a4",
            link="https://discuss.streamlit.io/t/new-component-react-bootstrap-carousel/46819",
        ),
        dict(
            title="Slide 2",
            text="A wooden bridge in a forest in Autumn",
            img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
            link="https://github.com/thomasbs17/streamlit-contributions/tree/master/bootstrap_carousel",
        ),
        dict(
            title="Slide 3",
            text="A distant mountain chain preceded by a sea",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
            link="https://github.com/thomasbs17/streamlit-contributions/tree/master",
        ),
        dict(
            title="Slide 4",
            text="PANDAS",
            img="pandas.webp",
        ),
        dict(
            title="Slide 4",
            text="CAT",
            img="cat.jpg",
        ),
    ]

    carousel(items=test_items)

