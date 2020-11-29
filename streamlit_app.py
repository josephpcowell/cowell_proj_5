"""
This .py is the structure for the Streamlit app associated with
the corresponding project on generating The Beatles lyrics.
"""

# Import streamlit
import streamlit as st

# Import the usual suspects
import pandas as pd
import numpy as np
import pickle

# from generator import gen_lyrics
# import generator

import os

import gpt_2_simple as gpt2
from datetime import datetime
import tensorflow

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from transformers import AutoTokenizer, GPT2Tokenizer

import os


# Select who will generate the song
singer = st.sidebar.selectbox(
    "Who is singing the song?",
    (
        "The Beatles",
        "John Lennon",
        "Paul McCartney",
        "George Harrison",
        "Ringo Starr",
    ),
)

# Change title based on songwriter
st.write(
    """# Song Generator: {}
""".format(
        singer
    )
)

# if singer == "The Beatles":
#     st.markdown(
#         """
#         <style>
#         .reportview-container {
#             background: url("https://upload.wikimedia.org/wikipedia/commons/8/87/The_Beatles_magical_mystery_tour_%28cropped%29.jpg");
#             background-position: center center;
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-blend-mode: lighten
#         }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )
# THE BACKGROUND ^

# if singer == "John Lennon":


# if singer == "Paul McCartney"


# if singer == "George Harrison"


# if singer == "Ringo Starr"


word = st.text_input(
    "Enter some lyrics to start the song:", value="here comes the sun"
)


if st.button("Generate"):

    if singer == "The Beatles":

        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(
            sess, checkpoint_dir="checkpoint_all", run_name="beatles"
        )
        text = gpt2.generate(
            sess,
            run_name="run1",
            length=500,
            temperature=1.0,
            top_k=0,
            top_p=0.9,
            prefix=word,
            return_as_list=True,
        )
        lyrics = text[0]
        st.write(lyrics)

    if singer == "George Harrison":

        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(
            sess, checkpoint_dir="checkpoint_all", run_name="harrison"
        )
        text = gpt2.generate(
            sess,
            run_name="run1",
            length=500,
            temperature=1.0,
            top_k=0,
            top_p=0.9,
            prefix=word,
            return_as_list=True,
        )
        lyrics = text[0]
        st.write(lyrics)

    if singer == "John Lennon":

        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(
            sess, checkpoint_dir="checkpoint_all", run_name="lennon"
        )
        text = gpt2.generate(
            sess,
            run_name="run1",
            length=500,
            temperature=1.0,
            top_k=0,
            top_p=0.9,
            prefix=word,
            return_as_list=True,
        )
        lyrics = text[0]
        st.write(lyrics)

    if singer == "Paul McCartney":

        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(
            sess, checkpoint_dir="checkpoint_all", run_name="mccartney"
        )
        text = gpt2.generate(
            sess,
            run_name="run1",
            length=500,
            temperature=1.0,
            top_k=0,
            top_p=0.9,
            prefix=word,
            return_as_list=True,
        )
        lyrics = text[0]
        st.write(lyrics)

    if singer == "Ringo Starr":

        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess, checkpoint_dir="checkpoint_all", run_name="starr")
        text = gpt2.generate(
            sess,
            run_name="run1",
            length=500,
            temperature=1.0,
            top_k=0,
            top_p=0.9,
            prefix=word,
            return_as_list=True,
        )
        lyrics = text[0]
        st.write(lyrics)

else:
    pass

st.write(
    """
_____
Check out the full repository
[here](https://github.com/josephpcowell/cowell_proj_5)
"""
)
