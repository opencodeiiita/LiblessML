import numpy as np
import pandas as pd

def print_success():
    print("\x1b[32m\"Success!!\"\x1b[0m")

def print_fail():
    print("\x1b[31m\"Failure!!\"\x1b[0m")

def is_set(category_less_than_25):
    return isinstance(category_less_than_25,set)

def is_dataframe(df):
    return isinstance(df,pd.DataFrame)

def check_small_category(category_less_than_25):
    if is_set(category_less_than_25):
        print_success()
    else:
        print_fail()
        print("For faster searching the category_less_than_25 should be a set")
    if len(category_less_than_25)==8:
        print_success()
    else:
        print_fail()
        print("The length of the set does not match")

def check_change_column_category(col_df):
    if is_dataframe(col_df):
        print_success()
    else:
        print_fail()
        print("The return type should be a dataframe")
    if col_df.shape==(3017,1):
        print_success()
    else:
        print_fail()
        print("The shape of the final dataframes do no match")

def check_column_to_one_hot(col_df,df):
    if is_dataframe(col_df):
        print_success()
    else:
        print_fail()
        print("The return type should be a dataframe")
    if col_df.shape==(3017,26):
        print_success()
    else:
        print_fail()
        print("The shape of the final dataframes do no match")
    if list(col_df.columns)==list(df['category'].unique()):
        print_success()
    else:
        print_fail()
        print("The column should be name of the unique category it denotes")