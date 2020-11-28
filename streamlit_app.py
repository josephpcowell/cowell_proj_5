"""
This .py is the structure for the Streamlit app associated with
the corresponding project on predicting fraudulent credit card transactions.
"""

# Import streamlit
import streamlit as st

# Import the usual suspects
import pandas as pd
import numpy as np
import pickle

from generator import gen_lyrics

import os

# Start of the app layout

st.write(
    """# Song Generator: The Beatles
"""
)

phrase = st.text_input(
    "Starting Phrase",
    value="Here comes the sun",
    max_chars=None,
    key=None,
    type="default",
)

lyrics = gen_lyrics(phrase)

st.write(lyrics)

st.write(
    """
_____
Check out the full repository
[here](https://github.com/josephpcowell/cowell_proj_5)
"""
)
