from env import get_db_url
from sklearn.model_selection import train_test_split

import pandas as pd
import acquire as aq
import wrangle as wr

"""
Contains CodeUp dataset functions for prepping data.
Author: Deangelo Bowen

"""

### split/prep zillow data function------------------------------------------------------
def split_zillow_data(zillow):
    """
    splits zillow data into train, test, validate 
    """
    train_validate, test = train_test_split(zillow, test_size=.2,
                                           random_state=123)
    train,validate = train_test_split(train_validate, test_size=.3,
                                     random_state=123)

    train = train.drop(columns=['tax_amount'])
    validate = validate.drop(columns=['tax_amount'])
    test = test.drop(columns=['tax_amount'])
    
    return train, validate, test


def prep_zillow(zillow):
    """
    Prepares zillow data by dropping nulls, renaming columns, removing outliers,
    and mapping certain values to new ones. 
    """
    zillow = zillow.dropna()
    zillow = zillow.rename(columns = {'bedroomcnt': 'bedrooms', 'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'sqft', 'yearbuilt':'year_built', 
                          'taxamount':'tax_amount', 'taxvaluedollarcnt':'tax_value'})

    columns = ['bedrooms','bathrooms','sqft','year_built','tax_amount','tax_value']
    zillow = wr.omit_outliers(zillow, 1.5, columns)

    
    zillow.fips = zillow.fips.map({6037.0: 'Los Angeles', 6059.0:'Orange County', 6111.0:'Ventura County'})

    train, validate, test = split_zillow_data(zillow)

    

    return train, validate, test


def prep_zillow_initial(zillow):
    zillow = zillow.dropna()
    zillow = zillow.rename(columns = {'bedroomcnt': 'bedrooms', 'bathroomcnt':'bathrooms', 
                          'calculatedfinishedsquarefeet':'sqft', 'yearbuilt':'year_built', 
                          'taxamount':'tax_amount', 'taxvaluedollarcnt':'tax_value'})

    columns = ['bedrooms','bathrooms','sqft','year_built','tax_amount','tax_value']
    zillow = wr.omit_outliers(zillow, 1.5, columns)
    
    zillow.fips = zillow.fips.map({6037.0: 'Los Angeles', 6059.0:'Orange County', 6111.0:'Ventura County'})

    return zillow
    
