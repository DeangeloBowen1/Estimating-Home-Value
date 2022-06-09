import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import acquire as aq
import prepare as pr
import explore as ex
import wrangle as wr
import math


from itertools import combinations
from scipy import stats
from scipy.stats import pearsonr, spearmanr

from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression 

from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures

warnings.filterwarnings('ignore')


# function to calculate quartile range and remove outliers
def omit_outliers(df, stdev, columns):
    for col in columns:
        
        # select quartiles
        q1, q3 = df[col].quantile([.25,.75]) 
        
        # calculate interquartile range
        iqr = q3 - q1
        
        upper_bound = q3 + stdev * iqr
        lower_bound = q1 - stdev * iqr
        
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
    return df




def wrangle_zillow():
    zillow_df = aq.get_zillow_data()
    df = zillow_df.dropna()
    df = df.rename(columns = {'bedroomcnt': 'bedrooms', 'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'sqft', 'yearbuilt':'year_built', 
                          'taxamount':'tax_amount', 'taxvaluedollarcnt':'tax_value'})
    
    column_list = df.columns[0:-1]
    df = omit_outliers(df, 1.5, column_list)
    
    df.fips = df.fips.map({6037.0: 'Los Angeles', 6059.0:'Orange County', 6111.0:'Ventura County'})
    
    return df


# create function to return scaled values
def scale_data(train, validate, test, return_scaler=False):
    """
    Scales split data
    
    If scaler = True, scaler object will be returned. Set to False. 
    """
    
    # scale the data
    scaled_cols = ['bedrooms', 'bathrooms', 'sqft']

    train_scaled = train.copy()
    validate_scaled = validate.copy()
    test_scaled = test.copy()

    scaler = MinMaxScaler()
    scaler.fit(train[scaled_cols])
    
    # now to transform

    train_scaled[scaled_cols] = scaler.transform(train[scaled_cols])
    validate_scaled[scaled_cols] = scaler.transform(validate[scaled_cols])
    test_scaled[scaled_cols] = scaler.transform(test[scaled_cols])
    
    if return_scaler:
        return train_scaled, validate_scaled, test_scaled, scaler
    else:
        return train_scaled, validate_scaled, test_scaled
