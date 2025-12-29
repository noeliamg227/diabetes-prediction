import pandas as pd

def aggregate_by_group(df: pd.DataFrame, group_var: str) -> pd.DataFrame:
    """
    Aggregate numeric features by a grouping variable.

    Parameters
    ----------
    df : pd.DataFrame
        Input dataframe
    group_var : str
        Column to group by (e.g., subject_id)

    Returns
    -------
    pd.DataFrame
        Aggregated dataframe
    """
    numeric_cols = df.select_dtypes(include="number").columns
    aggregated_df = (
        df.groupby(group_var)[numeric_cols]
        .mean()
        .reset_index()
    )
    return aggregated_df
