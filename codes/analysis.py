from streamlit.runtime.state import SessionState

from codes.utils.df import *
from codes.utils.general import toggle_button
from codes.weight_calc import score_pipeline
from config.paths import DS_PATH

DF = df_loader(DS_PATH).drop(["Project Name", "Type Name", "Unnamed: 0"], axis=1)
SESSION_STATE = SessionState()  # Create an instance of the custom SessionState class


def initial_analysis_view():
    df = DF.copy()
    toggle_button(SESSION_STATE, "initial", "Initially Extracted Smells", df)


def pivoted_analysis_view():
    df = DF.copy()
    df,_ = pivotiser(df)
    toggle_button(SESSION_STATE, "pivoted", "Package Pivoted Smells", df)


def aggregated_analysis_view():
    df = DF.copy()
    df = pivotiser_aggregator(df)
    toggle_button(SESSION_STATE, "aggregated", "Package Aggregated Smells", df)


def score_analysis_view():
    df = DF.copy()
    df = pivotiser_aggregator(df)
    df = score_pipeline(df)
    toggle_button(SESSION_STATE, "score", "Package Smell Score", df)

