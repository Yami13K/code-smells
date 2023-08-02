from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import streamlit as st


def profile_df(df):
    with open("static/eda.css", "r") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

    if df is not None:
        st.title("Exploratory Data Analysis")
        if st.button("Start EDA!"):
            # Perform profiling and generate the report
            profile_df = ProfileReport(
                df, title="Pandas Profiling Report", explorative=True
            )

            # Display the profiling report
            st_profile_report(profile_df)
    else:
        st.warning("Please upload a dataset first to perform profiling.")
