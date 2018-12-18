import pandas as pd
import numpy as np

from sklearn import metrics

from global_variables import *

def handle_missing_values(df):
    for col in create_NA_cat_features:
        df[col].fillna(value='NA', inplace=True)

    for col in create_none_cat_features:
        df[col].fillna(value='None', inplace=True)

    for col in fill_mean_features:
        df[col].fillna(value=df[col].mean(), inplace=True)

    df.Electrical.fillna(value='Mix', inplace=True)

    df.drop(large_null_features, axis=1, inplace=True)
    
    for col in fill_most_common_cat_features:
        df[col].fillna(value=df[col].value_counts().idxmax(), inplace=True)
        
        
def rmse(y_test, y_pred):
    return np.sqrt(metrics.mean_squared_error(y_test, y_pred))