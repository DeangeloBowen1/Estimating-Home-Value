import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydataset
import seaborn as sns


from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer

from sklearn.model_selection import train_test_split
from scipy import stats as stats
from itertools import combinations


import warnings
warnings.filterwarnings("ignore")

import acquire as aq
import prepare as prep



def plot_variable_pairs(df):

    """
    Plots features in pairs for a side-by-side comparison of features in a regression plot (lmplot)
    """
    
    column = ['bedrooms', 'bathrooms', 'sqft', 
                'year_built']
    
    columns= combinations(column, 2)
    
    for col in columns:
        sns.lmplot(data = df.sample(1000), x=col[1] , y=col[0],
                   col = 'fips',
                   hue='fips',line_kws={'color': 'red'} )
    return



def plot_categorical_and_continuous_vars_displot(df):

    """
    Creates a displot of select columns in a dataframe
    """
    
    columns = ['bedrooms', 'bathrooms', 'sqft',
                'tax_value']

    for col in columns:
        plt.figure(figsize=(10, 13))
        sns.displot(data = df, x=col, hue='fips', element="step")
        
        plt.show()
    
    return

def plot_categorical_and_continuous_vars_swarmplot(df):

    """
    Creates a swarmplot of select columns in a dataframe
    """

    columns = ['bedrooms', 'bathrooms', 'sqft',
                'tax_value']
    
    for col in columns:
        plt.figure(figsize=(7, 8))
        sns.swarmplot(data=df, x='fips', y=col)
        
        plt.show()
    
    return

def plot_categorical_and_continuous_vars_violinplot(df):

    """
    Creates a violinplot of select columns in a dataframe
    """

    columns = ['bedrooms', 'bathrooms', 'sqft',
                'tax_value']

    for col in columns:
        plt.figure(figsize=(10,5))
        plt.xlabel(col)
        sns.violinplot(x = df.fips, y = df[col], split =True,
                       scale='count')
        plt.show()
    
    return

def zillow_lmplot(df):
    """

    Takes in the train dataframe for the zillow dataset and returns an lmplot
    
    """
    plt.figure(figsize=(12,8))
    sns.lmplot(x='sqft', y='tax_value',
                data = df.sample(1000), hue = 'fips', size = 8)
    plt.show()
    return

def get_orange_county_data(df):

    """
    Takes in the train dataframe for the zillow dataset and targets homes under
    orange county to retrieved bedroom and bathroom information
    
    """
    orangecounty_data = df[df.fips == 'Orange County']

    plt.figure(figsize=(10,8))
    sns.barplot(data=orangecounty_data, y='tax_value', x='bedrooms')
    plt.show()

    plt.figure(figsize=(10,8))
    sns.barplot(data=orangecounty_data, y='tax_value', x='bathrooms')
    plt.show()
    return

def bathroom_lmplot(df):
    sns.lmplot(x='sqft', y='bathrooms', data=df, size = 5, 
           line_kws={'color':'red'})
    return

def bathroom_ttest(df):
    # set the alpha
    alpha = 0.05


    t, p = stats.ttest_ind(df.sqft, df.bathrooms, equal_var=False)

    if p /2 > alpha:
        print('I fail to rejext the null hypothesis, that there is no linear correlation between square feet and number of bedrooms.')
    elif t < 0:
        print('I fail to rejext the null hypothesis, that there is no linear correlation between square feet and number of bedrooms.')
    else:
        print('I reject the null hypothesis that there is no linear correlation between square feet and number of bedrooms. ')



def year_and_value(df):
    """
    Creates a lmplot of years built and total tax value columns in the zillow dataframe
    """
    sns.lmplot(x='year_built', y='tax_value', data=df.sample(10_000), size = 12, 
           line_kws={'color':'red'})





def year_ttest(df):

    """
    A statistical T-Test for a linear correlation between total home value and the year the home was built
    """
    # set the alpha
    alpha = 0.05


    t, p = stats.ttest_ind(df.tax_value, df.year_built, equal_var=False)

    if p /2 > alpha:
        print('I fail to rejext the null hypothesis, that there is no linear correlation between total home value and the year the home was built.')
    elif t < 0:
        print('I fail to rejext the null hypothesis, that there is no linear correlation between total home value and the year the home was built.')
    else:
        print('I reject the null hypothesis that there is no linear correlation between total home value and the year the home was built.')


    
def visualize_scaler(scaler, df, target):
    """
    Visualizes before and after scaling for features in a dataframe. 
    """
    fig, axs = plt.subplots(len(target), 2, figsize=(16,12))
    df_scaled = df.copy()
    df_scaled[target] = scaler.fit_transform(df[target])
    
    for (ax1, ax2), col in zip(axs, target):
        ax1.hist(df[col])
        ax1.set(title=f'{col} before scaling the data', xlabel=col, ylabel='count')
        ax2.hist(df_scaled[col])
        ax2.set(title=f'{col} data after scaling', xlabel=col, ylabel='count')
    plt.tight_layout()
    plt.show()
    return fig, axs
