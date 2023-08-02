import streamlit as st
import pandas as pd
from .utils_df import *
from codes.utils import toggle_button
from config.paths import DS_PATH

DF = df_loader(DS_PATH)


def initial_analysis_view():
    # file = st.file_uploader("Upload Your Dataset")
    # if file:
    #     df = pd.read_csv(file, index_col=None)
    #     df.to_csv(DS_PATH, index=None)
    #
    # if st.button('Show')
    df = DF.copy()
    toggle_button("initial", "Initially Extracted Smells", df)
