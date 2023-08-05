from matplotlib import pyplot as plt
import seaborn as sns
from codes.utils.df import df_loader
from codes.utils.general import styler
from codes.weight_calc import score_pipeline
from config.paths import DS_PATH
import streamlit as st

from config.static import WARNING


def score_analysis_view(df):
    styler('eda')
    _, col = st.columns([1, 7])
    with col:
        st.title("Scores Data Analysis")
    if df is not None:
        button_placeholder = st.empty()

        if button_placeholder.button("show scores!"):
            st.subheader("Score Dataframe")
            score_df = score_pipeline(df)
            button_placeholder.empty()

            cols = st.columns([2, 7, 2])
            with cols[1]:
                st.dataframe(
                    score_df.style.highlight_max(axis=0),
                    width=1000,
                )
            kde(score_df)
    else:
        st.warning(WARNING)


def kde(scores_df):
    st.subheader("Probability Density Function")
    # Create a KDE plot of the 1D data
    sns.kdeplot(scores_df, color="blue", fill=True)
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.title("KDE Plot of 1D Data")
    st.pyplot(plt)
