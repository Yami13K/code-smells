import pandas as pd
import streamlit as st


class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def toggle_button(
    session_state: SessionState, session_var: str, title: str, df: pd.DataFrame, button_text: str = "Toggle"
):
    col1, col2 = st.columns([4, 1])  # Adjust column widths as needed
    col1.title(title)

    # Add a button to show/hide the DataFrame
    if col2.button(button_text, key=session_var):
        if not hasattr(session_state, session_var):
            setattr(session_state, session_var, True)  # Initialize state variable

        setattr(session_state, session_var, not getattr(session_state, session_var))

    # Display DataFrame based on button state
    if hasattr(session_state, session_var) and getattr(session_state, session_var):
        st.dataframe(df)
