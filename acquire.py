from env import host, user, password, get_db_url
import pandas as pd 
import os

def get_zillow_data(use_cache=True):
    filename = 'zillow.csv'
    if os.path.isfile(filename) and use_cache:
        return pd.read_csv(filename)
    else:
        df = pd.read_sql('''
        SELECT bathroomcnt, bedroomcnt, taxvaluedollarcnt, taxamount,
        calculatedfinishedsquarefeet, yearbuilt, fips
        FROM properties_2017 
        LEFT JOIN predictions_2017 USING (parcelid) 
        LEFT JOIN propertylandusetype USING (propertylandusetypeid)
        WHERE propertylandusedesc IN ('Single Family Residential',
        'Inferred Single Family Residential') 
        AND YEAR(transactiondate) = 2017;''', get_db_url('zillow'))
        df.to_csv(filename, index=False)
        return df
