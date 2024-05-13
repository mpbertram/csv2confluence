from pandas import DataFrame


def disjunct(df1: DataFrame, df2: DataFrame) -> DataFrame:
    p1 = df1.copy()
    p2 = df2.copy()

    indices = p2.columns.values.tolist()
    p1.set_index(indices, inplace=True)
    p2.set_index(indices, inplace=True)

    return df1[~p1.index.isin(p2.index.values)]


def intersection(df1: DataFrame, df2: DataFrame) -> DataFrame:
    p1 = df1.copy()
    p2 = df2.copy()

    indices = p2.columns.values.tolist()
    p1.set_index(indices, inplace=True)
    p2.set_index(indices, inplace=True)

    return df1[p1.index.isin(p2.index.values)]
