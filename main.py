""" This file contains the code to run a simple web app using streamlit to generate linkedin posts"""

import streamlit as st
from generator import generate_post
from filter_post import FilterPosts

size_options = ["Short", "Medium", "Long"]
lang_options = ["English", "Hinglish"]

def main():
    # create web app

    st.title("LinkedIn Post AI")
    fp = FilterPosts()
    col1, col2, col3 = st.columns(3)

    with col1:
        topic = st.selectbox("Topic", options=fp.get_tags())

    with col2:
        size = st.selectbox("Size", options=size_options)

    with col3:
        lang = st.selectbox("Language", options=lang_options)

    if st.button("Generate"):
        post = generate_post(topic, size, lang)
        st.write(post)

if __name__ == "__main__":
    main()