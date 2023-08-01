import streamlit as st


def set_custom_theme():
    # Define your custom theme colors
    primary_color = "#04c4e6"

    # Set the custom theme
    st.set_page_config(
        page_title="AHP Matrix Input",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="auto",
    )
