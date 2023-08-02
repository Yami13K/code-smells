import streamlit as st
from pycaret.regression import setup, compare_models, pull, save_model
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
import os
from codes.ahp import ahp_view
from pandas_profiling import ProfileReport

from codes.analysis import initial_analysis_view
from codes.github import git_url_view
from config.paths import *
from config.theme import set_custom_theme


def main():
    if os.path.exists(DS_PATH):
        df = pd.read_csv(DS_PATH, index_col=None)
    else:
        df = None

    with st.sidebar:
        st.image(IMAGE_URL)
        st.title(APP_TITLE)
        choice = st.radio("Navigation", ["Git Repo", "AHP picker", "Modelling", "Download"])
        st.info("This project application helps you build and explore your data.")

    if choice == "Git Repo":
        git_url_view()
        initial_analysis_view()
        # if df is not None:  # Check if df is available before performing profiling
        #     st.title("Exploratory Data Analysis")
        #     profile_df = df.profile_report()
        #     st_profile_report(profile_df)
        # else:
        #     st.warning("Please upload a dataset first to perform profiling.")

    if choice == "AHP picker":
        # st.title("Upload Your Dataset")
        # file = st.file_uploader("Upload Your Dataset")
        # if file:
        #     df = pd.read_csv(file, index_col=None)
        #     df.to_csv(DS_PATH, index=None)

        ahp_view()



    if choice == "Modelling":
        if df is not None:  # Check if df is available before running the model
            chosen_target = st.selectbox("Choose the Target Column", df.columns)
            if st.button("Run Modelling"):
                setup(df, target=chosen_target, silent=True)
                setup_df = pull()
                st.dataframe(setup_df)
                best_model = compare_models()
                compare_df = pull()
                st.dataframe(compare_df)
                save_model(best_model, "best_model")
        else:
            st.warning("Please upload a dataset first to perform modeling.")

    if choice == "Download":
        if os.path.exists("best_model.pkl"):
            with open("best_model.pkl", "rb") as f:
                st.download_button("Download Model", f, file_name="best_model.pkl")
        else:
            st.warning(
                "The model has not been generated yet. Please run the modeling step first."
            )


if __name__ == "__main__":
    main()
