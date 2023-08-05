from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
import streamlit as st

from codes.utils.general import styler
from config.static import WARNING


def profile_df(df):
    styler("eda")

    if df is not None:
        _, col = st.columns([1, 13])
        with col:
            st.title("Exploratory Data Analysis")

        # Use st.empty() to create a placeholder for the button
        button_placeholder = st.empty()

        if button_placeholder.button("Start EDA!"):
            # Perform profiling and generate the report
            profile_df = ProfileReport(
                df, title="Pandas Profiling Report", explorative=True
            )

            # Display the profiling report
            st_profile_report(profile_df)

            # Clear the button placeholder
            button_placeholder.empty()
    else:
        st.warning(WARNING)
