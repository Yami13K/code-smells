import pandas as pd


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
        smell: [val for val in column_names if smell in val] for smell in smells
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
