import streamlit as st
from contextlib import contextmanager
from io import StringIO
from streamlit.report_thread import REPORT_CONTEXT_ATTR_NAME
from threading import current_thread
import sys

from aitextgen import aitextgen

# loading in the trained model
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

ai = aitextgen(model_folder="/Users/logno/Documents/GitHub/conspiracy_generation/models/trained_model", to_gpu=False)

@contextmanager
def st_redirect(src, dst):
    placeholder = st.empty()
    output_func = getattr(placeholder, dst)

    with StringIO() as buffer:
        old_write = src.write

        def new_write(b):
            if getattr(current_thread(), REPORT_CONTEXT_ATTR_NAME, None):
                buffer.write(b)
                output_func(buffer.getvalue())
            else:
                old_write(b)

        try:
            src.write = new_write
            yield
        finally:
            src.write = old_write

@contextmanager
def st_stdout(dst):
    with st_redirect(sys.stdout, dst):
        yield

@contextmanager
def st_stderr(dst):
    with st_redirect(sys.stderr, dst):
        yield

def generate(user_input) -> str:
    return ai.generate_one(max_length=200, prompt=user_input, min_length=100, temperature=1.0, top_p=0.9)

def main():
    form = st.form(key='my-form')
    input = form.text_input('Enter your conspiracy here')
    submit = form.form_submit_button('Generate')

    st.write('Press generate to generate a conspiracy theory!')

    if submit:
        with st_stdout("markdown"):
            print(generate(input).replace('*',''))

if __name__=='__main__': 
    main()