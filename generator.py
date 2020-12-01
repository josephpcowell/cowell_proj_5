# % tensorflow_version 1.x
import gpt_2_simple as gpt2
from datetime import datetime
import tensorflow

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from transformers import AutoTokenizer, GPT2Tokenizer

import os

# sess = gpt2.start_tf_sess()
# gpt2.load_gpt2(sess, checkpoint_dir="beatles_mod1", run_name="run1")


def gen_lyrics(phrase):

    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, checkpoint_dir="beatles_mod1", run_name="run1")

    text = gpt2.generate(
        sess,
        run_name="run1",
        length=500,
        temperature=1.0,
        top_k=0,
        top_p=0.9,
        prefix=phrase,
        return_as_list=True,
    )

    return text[0]
