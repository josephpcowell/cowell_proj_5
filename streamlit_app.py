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
import string

import gpt_2_simple as gpt2
from datetime import datetime
import tensorflow

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from transformers import AutoTokenizer, GPT2Tokenizer

import os

# Set background image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://lh3.googleusercontent.com/eN3HuiVn82pEi7T1IDq0asKc8BFO2d8OPx0psLlm-OzWHhy7yW97FUoDYv9pkaZGvFggsnCzRkHi3aMBmydVN__9unpAY8cW2Ev0looC0mqZQ0aZprtKJ63pTbY4gH8qL5d9r069IpKJGU5pW5Y5CCZ4E2dRoXdgUT8h4ZQv0EgkPdxrSs5bHYsvJhBtHKNboeyTIdDLW39EOCAkxfqWlufypKFhQukpIts7TIuRs3LrRxz-6dEce0TV3sCFgF7R5qpalvLSq_bh8IjggFs6UCpY9H3zcKQVXaddL9-CTVdG3nXhPISEj1DYApv6ZNtlEOB6A0aPuOa0fQTF8r2fEh8j2_q2bpMMGO8mB5oH8Lbrg0J8j6Bm1i1I7LD2f3YtJusw64lNUABUCDNtfJXiNN1M5RB4AGZi_huS5AYjCewAO6PBG7yKOG64G2NJYq8gZjK40g3XUgchBgpTHg7Lf-mVneTzky_EbqWGSN78sp1AfkWSysTTTusshS-PC87LxKn0TLjGFh8lRT4MT1iMQQFRxid15LOY4pOgWnPp4FK7OpeNkoA7TfOvO7r0nxTpoGCZzQhzN1V59FQl7Gt3boFeYuiOwcg0JoV9CrhBVywe6eHoMSFgzoByGJPA5FUz5xPz2pHyM-A8Ls3SoybtrSf2dhE7NLRNt6Fp62_NVkE7aslcF6v7w3ycXppwoA=w1479-h946-no?authuser=0");
        background-position: right;
        background-size: cover;
        background-repeat: no-repeat;
        background-blend-mode: lighten
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
<style>
.reportview-container .markdown-text-container {
    font-family: 'Arial Black', sans-serif;
}
<\style>
""",
    unsafe_allow_html=True,
)

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

# Sidebar Images
if singer == "The Beatles":
    st.markdown(
        """
    <style>
    .sidebar .sidebar-content {
            background: url("https://lh3.googleusercontent.com/pw/ACtC-3foSA1xcxpvR9KE_H58nAG4MXgOatpwyz0L0HqPsfWTekxbilKXhTXe3XbHmh7G2kv_yN9lHcGXvp2vvTUAjGYM3Rfk4MPx_gYFsF5gkWz3tRB7DFYonjfpxiEgz21R4AwNTZsoH-BAdCCFP-gFZhIp=w379-h946-no?authuser=0");
            background-position: center center;
            background-size: cover;
            background-repeat: no-repeat;
            background-blend-mode: lighten;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

if singer == "John Lennon":
    st.markdown(
        """
    <style>
    .sidebar .sidebar-content {
            background: url("https://lh3.googleusercontent.com/pw/ACtC-3f-LsTo2ut2EJYrN2CNSv-oAA9R2v-gc-5Otpquu97-toKZuvnIWtbmkgXfBpKgV6EXimfXttmrEqT0pjMPLeWwmeEuz5glnKgMrACn2oDxurBfOPudMCqpLFMjtlKv62OGItXYTM226ag1pejgX3XT=w379-h946-no?authuser=0");
            background-position: center center;
            background-size: cover;
            background-repeat: no-repeat;
            background-blend-mode: lighten
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

if singer == "Paul McCartney":
    st.markdown(
        """
    <style>
    .sidebar .sidebar-content {
            background: url("https://lh3.googleusercontent.com/pw/ACtC-3c0M97Fe6jfaeMiEgh2x5-djA5SzY3mxdRIxHMYxWV-gSdoK07quCQGvq85JNLsjo8FE7ecdjM05UjY10qIdvhpymlQ3JIuGGkiUWAHYGpvy68TQ3dLO062nOCL3N88j1DcsORq0cGOV8nxxwWAAKPC=w379-h946-no?authuser=0");
            background-position: center center;
            background-size: cover;
            background-repeat: no-repeat;
            background-blend-mode: lighten
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

if singer == "George Harrison":
    st.markdown(
        """
    <style>
    .sidebar .sidebar-content {
            background: url("https://lh3.googleusercontent.com/pw/ACtC-3eFESjQaPpPgZiX3979ztPwxRqG_Yryi78ur8DxGSHxx2CfeOSJYAp2M7gn-AxOd9a9xHAjkF4N5-s6FwMYUJoQQ8dKzm10P5Z8dcIJdnnL0ua_ct1vJ5y7LktaED3jTgigpd02H7FqkB3FaAA0i5pd=w379-h946-no?authuser=0");
            background-position: center center;
            background-size: cover;
            background-repeat: no-repeat;
            background-blend-mode: lighten
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

if singer == "Ringo Starr":
    st.markdown(
        """
    <style>
    .sidebar .sidebar-content {
            background: url("https://lh3.googleusercontent.com/pw/ACtC-3c3GIZr_EoLcNre0GvROBF6plrHVZ3Go-F788QjsRKhE6UCqABb-QQ5Yqgk0j3N7l7FMAg0IWb753zBI6hUbVusGX_5c07on8ObZlTLxn67G7Umy3p9H6i3LsgIR2iqjeFPhY44ibNqaPwCqHtRCnYE=w379-h946-no?authuser=0");
            background-position: center center;
            background-size: cover;
            background-repeat: no-repeat;
            background-blend-mode: lighten
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

# User input

word = st.text_input(
    "Enter some lyrics to start the song:", value="Here comes the sun"
)

# Text generation

if st.button("Generate"):

    if singer == "The Beatles":

        # Model for generating text
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

        # Formatting text for output

        lyrics = text[0]
        split = lyrics.splitlines()

        verse1 = split[:4]
        verse1 = "\n".join(verse1)

        verse2 = split[4:8]
        verse2 = "\n".join(verse2)

        chorus = split[8:12]
        chorus = "\n".join(chorus)

        bridge = split[12:16]
        bridge = "\n".join(bridge)

        st.write("Title: " + string.capwords(split[11]))

        st.write("Verse 1")
        st.text(verse1)

        st.write("Chorus")
        st.text(chorus)

        st.write("Verse 2")
        st.text(verse2)

        st.write("Chorus")
        st.text(chorus)

        st.write("Bridge")
        st.text(bridge)

        st.write("Chorus")
        st.text(chorus)

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
        # Formatting text for output

        lyrics = text[0]
        split = lyrics.splitlines()

        verse1 = split[:4]
        verse1 = "\n".join(verse1)

        verse2 = split[4:8]
        verse2 = "\n".join(verse2)

        chorus = split[8:12]
        chorus = "\n".join(chorus)

        bridge = split[12:16]
        bridge = "\n".join(bridge)

        st.write("Title: " + string.capwords(split[11]))

        st.write("Verse 1")
        st.text(verse1)

        st.write("Chorus")
        st.text(chorus)

        st.write("Verse 2")
        st.text(verse2)

        st.write("Chorus")
        st.text(chorus)

        st.write("Bridge")
        st.text(bridge)

        st.write("Chorus")
        st.text(chorus)

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
        # Formatting text for output

        lyrics = text[0]
        split = lyrics.splitlines()

        verse1 = split[:4]
        verse1 = "\n".join(verse1)

        verse2 = split[4:8]
        verse2 = "\n".join(verse2)

        chorus = split[8:12]
        chorus = "\n".join(chorus)

        bridge = split[12:16]
        bridge = "\n".join(bridge)

        st.write("Title: " + string.capwords(split[11]))

        st.write("Verse 1")
        st.text(verse1)

        st.write("Chorus")
        st.text(chorus)

        st.write("Verse 2")
        st.text(verse2)

        st.write("Chorus")
        st.text(chorus)

        st.write("Bridge")
        st.text(bridge)

        st.write("Chorus")
        st.text(chorus)
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
        # Formatting text for output

        lyrics = text[0]
        split = lyrics.splitlines()

        verse1 = split[:4]
        verse1 = "\n".join(verse1)

        verse2 = split[4:8]
        verse2 = "\n".join(verse2)

        chorus = split[8:12]
        chorus = "\n".join(chorus)

        bridge = split[12:16]
        bridge = "\n".join(bridge)

        st.write("Title: " + string.capwords(split[11]))

        st.write("Verse 1")
        st.text(verse1)

        st.write("Chorus")
        st.text(chorus)

        st.write("Verse 2")
        st.text(verse2)

        st.write("Chorus")
        st.text(chorus)

        st.write("Bridge")
        st.text(bridge)

        st.write("Chorus")
        st.text(chorus)

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
        # Formatting text for output

        lyrics = text[0]
        split = lyrics.splitlines()

        verse1 = split[:4]
        verse1 = "\n".join(verse1)

        verse2 = split[4:8]
        verse2 = "\n".join(verse2)

        chorus = split[8:12]
        chorus = "\n".join(chorus)

        bridge = split[12:16]
        bridge = "\n".join(bridge)

        st.write("Title: " + string.capwords(split[11]))

        st.write("Verse 1")
        st.text(verse1)

        st.write("Chorus")
        st.text(chorus)

        st.write("Verse 2")
        st.text(verse2)

        st.write("Chorus")
        st.text(chorus)

        st.write("Bridge")
        st.text(bridge)

        st.write("Chorus")
        st.text(chorus)

else:
    pass

# Contact and Github

# st.markdown(
#     """
# #
# ---
# App by Joe Cowell
# Check out the full repository
# [here](https://github.com/josephpcowell/cowell_proj_5)
# Reach Out: [LinkedIn](https://www.linkedin.com/in/josephpcowell/)
# [Medium](https://josephpcowell.medium.com/)
# """
# )
