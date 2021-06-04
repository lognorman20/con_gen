import streamlit as st
from contextlib import contextmanager
from io import StringIO
from streamlit.report_thread import REPORT_CONTEXT_ATTR_NAME
from threading import current_thread

import sys

import random

from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

from aitextgen import aitextgen

# loading in the trained model
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

hash_funcs={'_io.TextIOWrapper' : lambda _: None}

@st.cache(allow_output_mutation=True, max_entries=1, ttl=None)
def load_model():
    ai = aitextgen(model_folder="models/trained_model", to_gpu=False)
    return ai

@st.cache(allow_output_mutation=True, max_entries=1, ttl=None)
def load_topics():
    topics = ['Gnosticism, Archons & the Demiurge', 'Antarctica', 'The Moon, Phobos & Solar System Anomalies',
    'Nikola Tesla, Zero Point Energy, the Philadelphia Experiment & the Suppression of Advanced Technology', 'MKULTRA',
    'Medical Conspiracies', 'Nibiru, Enki/Enlil & Zecharia Sitchin', 'Mystery Schools, Secret Societies & Ancient America', 'Bankers, Oligarchs, One World Government, and the Attack on American Sovereignty',
    'Unified Physics & the Mechanics of Consciousness: Religion, the Occult, Psychedelics, UFO Tech and the Holographic Universe', 'Aleister Crowley, Satanic Cults, and the Franklin Cover-up', 'Atlantis, Lemuria, Lost Civilizations & Ancient High Technology','Pizza/PedoGate and Human Sex Trafficking','Ghosts, Possessions, Psychic Phenomena & the Afterlife', 'The Intentional Addictiveness of Smart Devices and the Short & Long Term Effects of "Smart" Tech on Society'
    'Solutions', 'The Cult of Science', 'The Past, Present & Future of /r/conspiracy', 'Human Potential', 'Cryptids', 'Usury, the Money Changers, and the Alchemy of High Finance', 'Big Pharma, Psychotropics & Mass Shootings', "Earth's Catastrophe Cycles", 'Tartaria, Cultural Layer/Mudflood & Phantom Time',
    'Sacred Geometry, Cymatics, EMF Exposure, and the Effect of 5G on Biological Entities', 'Deep Underground Military Bases, Area 51, & CERN', 'Adrenochrome & Human Trafficking', 'The Cult of Saturn & the Black Cube', 'Media as Propaganda', 'Alien Presence on Earth']
    return topics

ai = load_model()
topics = load_topics()

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

@st.cache(hash_funcs=hash_funcs)
def main():
    st.markdown("<h1 style='text-align: center;'>Conspiracy Theory Generator</h1>", unsafe_allow_html=True)
    st.write('\n'*2)

    with st.beta_expander("Conspiracy Topic Ideas"):
        for topic in topics:
            st.write(topic)

    form = st.form(key='my-form')
    st.markdown('<p style="text-align: center;">Example inputs: "I am starting to believe aliens", "I think the moon landing", "My theory about vaccines is"</p>', unsafe_allow_html=True)
    input = form.text_input('Enter your conspiracy here')
    submit = form.form_submit_button('Generate')


    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    if submit:
        waiting_texts = ['Asking randoms on Reddit...','Confirming with the Illuminati...','Consulting with the aliens...', 
        'Looking in the tunnels of Denver International Airport...', 'Discussing with Barack Obama...',
        'Getting approval from Jeffrey Epstein...', 'Double-checking with Kanye West...']
        with st.spinner(waiting_texts[random.randint(0,6)]):
            with st_stdout("markdown"):
                print(generate(input).replace('*',''))


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))

def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)

def layout(*args):

    style = """
    <style>

      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="white",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

def footer():
    myargs = [
        "Made in ",
        image('https://streamlit.io/images/brand/streamlit-mark-color.svg',
              width=px(25),height=px(25)),
        " by ",
        link("https://www.linkedin.com/in/logannorman/", "Logan Norman"),
        br()
    ]
    layout(*myargs)

if __name__=='__main__': 
    main()
    footer()