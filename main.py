import streamlit as st

st.set_page_config(layout='wide')


with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.image("images/photo.png")
    with col2:
        st.title("Joe Smith")
        content = """
        Hi I am Joe
        """
        st.info(content)


summary = """
Below you can find some of the apps
I have built in Python."""
st.info(summary)
