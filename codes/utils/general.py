import os
import time

import pandas as pd
import streamlit as st
import numpy as np
from pycaret.clustering import plot_model


def softmax(x):
    # Numerical stability: subtract the maximum value from each element
    # to avoid large exponential values that might cause overflow.
    max_x = np.max(x)
    x_exp = np.exp(x - max_x)
    sum_x_exp = np.sum(x_exp)
    softmax_output = x_exp / sum_x_exp
    return softmax_output


class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


def toggle_button(
    session_state,
    session_var,
    title,
    data,
    button_text="Toggle",
):
    col1, col2 = st.columns([4, 1])  # Adjust column widths as needed
    col1.subheader(title)

    if not hasattr(session_state, session_var):
        setattr(session_state, session_var, False)
    disabled = True if data is None else False
    # Add a button to show/hide the DataFrame
    if col2.button(button_text, key=session_var, disabled=disabled):
        setattr(session_state, session_var, not getattr(session_state, session_var))

    # Display DataFrame based on button state
    if hasattr(session_state, session_var) and getattr(session_state, session_var):
        st.dataframe(data)


def title_plot(results, plot: str):
    st.title(plot.capitalize() + "Plot")
    # Create the plot using plot_model from PyCaret
    plot_model(results, plot=plot)


def styler(file_name):
    with open(f"static/{file_name}.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)


def exists(DS_PATH):
    if os.path.exists(DS_PATH):
        return pd.read_csv(DS_PATH, index_col=None)
    else:
        return None


def toast(file="AHP Matrix"):
    msg = st.toast(f":blue[{file} is processing..]")
    time.sleep(2)
    msg.toast(f":blue[finalizing...]")
    time.sleep(1)
    msg.toast(f":green[{file} Secured!]", icon="✅")



