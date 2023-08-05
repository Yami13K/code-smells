import time

import streamlit as st
import pandas as pd
import os
from codes.ahp import ahp_view
from codes.analysis import (
    aggregated_analysis_view,
    initial_analysis_view,
    pivoted_analysis_view,
)
from codes.clustering import clusterize
from codes.github import git_url_view
from codes.mapper import ck_mapper_view
from codes.profiling import profile_df
from codes.scores import kde, score_analysis_view
from codes.utils.general import exists
from codes.weight_calc import score_pipeline
from config.paths import *
from config.static import NAVIGATION


def main():
    st.set_page_config(page_title="ReliaMain", page_icon="🔧")

    df = exists(DS_PATH)
    with st.sidebar:
        st.image(IMAGE_URL)
        st.title(APP_TITLE)
        choice = st.radio("Navigation", NAVIGATION, index=0)
        st.info("Maintenance index app")

    if choice == "Git Repo":
        git_url_view()
        initial_analysis_view(df)
        pivoted_analysis_view(df)
        aggregated_analysis_view(df)

    if choice == "Scores":
        score_analysis_view(df)

    if choice == "AHP picker":
        ahp_view()

    if choice == "Mapper":
        ck_mapper_view()

    if choice == "Profiling":
        profile_df(df)

    if choice == "Clustering":

        clusterize(df)


if __name__ == "__main__":
    main()
