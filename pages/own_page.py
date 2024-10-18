import streamlit as st

from utils.page_components import add_common_page_elements

sidebar_container = add_common_page_elements()

st.divider()

st.write("To make your own page create a page_name.py file and link to it in add_page_selector() in utils/page_components.py")
