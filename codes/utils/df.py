import pandas as pd

from config.static import SMELLS


def df_loader(path: str):
    df = pd.read_csv(path, index_col=None)
    return df


def df_saver(df: pd.DataFrame, path: str):
    df.to_csv(path, index=None)


def pivotiser(df):
    smell_counts = (
        df.groupby(["Package Name", "Code Smell"]).size().reset_index(name="Count")
    )
    pivot_table_df = smell_counts.pivot_table(
        index="Package Name", columns="Code Smell", values="Count", fill_value=0
    )
    pivot_table_df.reset_index(inplace=True)
    names = pivot_table_df.columns.to_list()
    return pivot_table_df, names


def smellizer(column_names):
    smells_dict = {
        smell: [val for val in column_names if smell in val] for smell in SMELLS
    }
    return smells_dict


def aggregator(func):
    def wrapper(*args):
        pivot_table_df, names = func(*args)
        smells_dict = smellizer(names)
        aggregated_df = pd.DataFrame(
            {
                "Package Name": pivot_table_df["Package Name"],
                **{
                    smell_key: pivot_table_df[smell_values].sum(axis=1)
                    for smell_key, smell_values in smells_dict.items()
                },
            }
        )
        return aggregated_df

    return wrapper


# function for pivotising and aggregating
pivotiser_aggregator = aggregator(pivotiser)


def normalize_records(df):
    df = df[df.columns[1:]]
    row_sums = df.sum(axis=1)
    df = df.div(row_sums, axis=0)
    return df


def weighted_sum(df, weight_array):
    df = df.mul(weight_array, axis=1)
    return df


def calculate_score(df, weighted_array):
    normalized_df = normalize_records(df)
    weighted_df = weighted_sum(normalized_df, weighted_array)
    df = pd.DataFrame(
        {"Package Name": df["Package Name"], "Score": weighted_df.sum(axis=1)}
    )
    df = df.set_index(df.columns[0])
    return df
