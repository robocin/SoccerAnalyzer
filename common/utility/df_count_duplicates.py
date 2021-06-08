import pandas as pd
import json

def df_count_duplicates(df, column_label):
    """
    Counts the duplicate rows by an specified column and what was the quantity
    :param df: dataframe
    :param column_label: column label you want to look for duplicates
    :return: json string with the duplicates and its quantities

    ex: lets say you have the following df:
    >> df
    show_time   value
    1             A
    2             B
    2             C
    3             D
    4             E
    4             F
    4             G
    5             G
    6             I
    >> json_string = df_count_duplicates(df, 'value')
    >> json_string
    {
        2: 2,
        4: 3
    }

    # ou seja, a linha cuja show_time era 2 apareceu duas vezes e a linha cuja sowtime era 4 apareceu 3 vezes.
    """

    full_column = df[column_label]

    count = 0
    is_counting = False
    instance_name = None
    dic = {}
    for i in range(0, len(full_column)):
        instances = 0
        if i > 0:
            if full_column[i] == full_column[i - 1]:
                if not is_counting:
                    is_counting = True
                    instance_name = full_column[i]
                    count = 2
                else:
                    count += 1
            else:
                if is_counting:
                    is_counting = False
                    dic[str(instance_name)] = str(count)

    return json.dumps(dic)
