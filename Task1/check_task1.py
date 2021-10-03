import numpy as np
import pandas as pd

def print_success():
    print("\x1b[32m\"Success!!\"\x1b[0m")

def print_fail():
    print("\x1b[31m\"Failure!!\"\x1b[0m")

def check_cleaned_data(df):
    expected_shape = (1971,10)
    any_null = any(df.isnull().any())
    if df.shape==expected_shape and not any_null:
        print_success()
    else:
        print_fail()

def is_indexed_properly(final_df):
    ind_arr = np.array(final_df.index)
    return len(np.unique(ind_arr))==len(ind_arr)

def is_balanced(final_df):
    final_df_dic = final_df['popularity'].value_counts().to_dict()
    return abs(final_df_dic['High']-final_df_dic['Low'])<150

def is_downsampled(final_df):
    final_df_dic = final_df['popularity'].value_counts().to_dict()
    return final_df_dic['High']==1448

def check_balanced_data(final_df):
    if is_indexed_properly(final_df):
        print_success()
    else:
        print_fail()
        print("DataFrame not indexed properly")
    if is_balanced(final_df):
        print_success()
    else:
        print_fail()
        print("DataFrame is not balanced on popularity for balancing abs(high-low)<150")
    if is_downsampled(final_df):
        print_success()
    else:
        print_fail()
        print("You are not allowed to chonge the size of the majority class")

def check_column(df):
    column = list(df.columns)
    if len(column)==9:
        print_success()
    else:
        print_fail()
    if 'app_id' not in column:
        print_success()
    else:
        print_fail()
