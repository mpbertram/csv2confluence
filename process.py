import os
import re
import pandas


def get_data(input_dir, delim=",", dict=None, agg_by=None, expand_fns=None, dtypes={}):
    data = {}

    for entry in os.scandir(input_dir):
        matches = re.search(".*\.csv", entry.name)
        if entry.is_file() and matches:
            csv = pandas.read_csv(entry.path, delimiter=delim, dtype=dtypes)

            if expand_fns is not None:
                expanded_csv = pandas.DataFrame()
                for col_name, col_fn in expand_fns.items():
                    idx = 0
                    for col in csv[col_name]:
                        df = col_fn(col)
                        for orig_col in csv.columns:
                            if orig_col != col_name:
                                df.insert(0, orig_col, csv.at[idx, orig_col])
                        expanded_csv = pandas.concat([expanded_csv, df])
                        idx = idx + 1
                csv = expanded_csv

            if dict is not None:
                csv.rename(inplace=True, columns=dict)

            if agg_by is not None:
                for agg in set(csv[agg_by]):
                    df = csv[csv[agg_by] == agg]
                    df = df.dropna(axis="columns", how="all")
                    if agg in data:
                        data.update({agg: pandas.concat([data[agg], df])})
                    else:
                        data.update({agg: df})
            else:
                data.update({entry.name: csv})

    return data
