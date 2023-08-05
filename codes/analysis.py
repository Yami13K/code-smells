from codes.utils.df import *


@drop_unrelated("initial", "Initially Extracted Smells")
def initial_analysis_view(df):
    return df


@drop_unrelated("pivoted", "Package Pivoted Smells")
def pivoted_analysis_view(df):
    df, _ = pivotiser(df)
    return df


@drop_unrelated("aggregated", "Package Aggregated Smells")
def aggregated_analysis_view(df):
    df = pivotiser_aggregator(df)
    return df
