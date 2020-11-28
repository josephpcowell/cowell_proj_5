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

# Start of the app layout
st.write(
    """# Song Generator: The Beatles
"""
)

word = st.text_input(
    "Enter some lyrics to start the song:", value="here comes the sun"
)

st.write("The current phrase is", word)


if st.button("Generate"):

    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, checkpoint_dir="beatles_mod1", run_name="run1")
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
# lyrics = gen_lyrics("hi")
else:
    pass

st.write(
    """
_____
Check out the full repository
[here](https://github.com/josephpcowell/cowell_proj_5)
"""
)
