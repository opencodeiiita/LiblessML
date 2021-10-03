import numpy as np
import pandas as pd

def print_success():
    print("\x1b[32m\"Success!!\"\x1b[0m")

def print_fail():
    print("\x1b[31m\"Failure!!\"\x1b[0m")

def is_dataframe(df):
    return isinstance(df,pd.DataFrame)

def is_float(df,col):
    return df.dtypes.to_dict()[col]=="float64"

def check_float_or_df(df,col):
    if is_dataframe(df):
        print_success()
    else:
        print_fail()
        print("The output should be a datframe")
    if is_float(df,col):
        print_success()
    else:
        print_fail()
        print("The column element should be float")

def check_clean_size(df):
    check_float_or_df(df,'size')

def check_clean_install(df):
    check_float_or_df(df,'installs')

def check_clean_price(df):
    check_float_or_df(df,'price')