import pandas as pd
import streamlit as st


def toggle_button(
    session_var: str, title: str, df: pd.DataFrame, button_text: str = "Toggle"
):
    col1, col2 = st.columns([4, 1])  # Adjust column widths as needed
    col1.title(title)

    # Add a button to show/hide the DataFrame
    if col2.button(button_text):
        if session_var not in st.session_state:
            st.session_state[session_var] = True  # Initialize state variable

        st.session_state[session_var] = not st.session_state[session_var]

    # Display DataFrame based on button state
    if session_var in st.session_state and st.session_state[session_var]:
        st.dataframe(df)
