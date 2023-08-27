import streamlit as st
import pandas as pd
import numpy as np
from CodeGPT import GPT_run

st.title('Code-GPT 🚀')

if st.button("Clear All"):
    # Clears all st.cache_resource caches:
    st.cache_resource.clear()

user_input = st.text_input(':violet[How can I help You?]', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder="What was the code of segment Trees?", disabled=False, label_visibility="visible")

def search():
    out = GPT_run(user_input)
    st.write(out.description); st.divider()
    st.code(out.code); st.divider()
    st.write(out.code_description); st.divider()
    st.code(out.input); st.divider()
    st.code(out.expected_output); st.divider()

st.button('search',on_click=search())




