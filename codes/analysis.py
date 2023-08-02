import streamlit as st
import pandas as pd
from streamlit.runtime.state import SessionState

from .utils_df import *
from codes.utils import toggle_button
from config.paths import DS_PATH

DF = df_loader(DS_PATH)
SESSION_STATE = SessionState()  # Create an instance of the custom SessionState class

def initial_analysis_view():
    df = DF.copy()
    toggle_button(SESSION_STATE, "initial", "Initially Extracted Smells", df)


def pivoted_analysis_view():
    df = DF.copy()
    df = pivotiser(df)
    toggle_button(SESSION_STATE, "pivoted", "Package Pivoted Smells", df)
