import streamlit as st
import pandas as pd
import os
from codes.ahp import ahp_view
from codes.analysis import (
    aggregated_analysis_view,
    initial_analysis_view,
    pivoted_analysis_view,
    score_analysis_view,
)
from codes.clustering import clusterize
from codes.github import git_url_view
from codes.profiling import profile_df
from codes.weight_calc import score_pipeline
from config.paths import *
from config.static import NAVIGATION


def main():
    if os.path.exists(DS_PATH):
        df = pd.read_csv(DS_PATH, index_col=None)
    else:
        df = None

    with st.sidebar:
        st.image(IMAGE_URL)
        st.title(APP_TITLE)
        choice = st.radio("Navigation", NAVIGATION, index=3)
        st.info("This project application helps you build and explore your data.")

    if choice == "Git Repo":
        git_url_view()
        initial_analysis_view()
        pivoted_analysis_view()
        aggregated_analysis_view()
        score_analysis_view()

    if choice == "AHP picker":
        ahp_view()

    if choice == "Profiling":
        profile_df(df)

    if choice == "Clustering":
        if df is None:
            st.warning(
                "The model has not been generated yet. Please run the modeling step first."
            )
        else:
            score_df = score_pipeline(df)
            clusterize(score_df)


if __name__ == "__main__":
    main()
