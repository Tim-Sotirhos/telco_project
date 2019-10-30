'''
Acquisition Phase:

Acquire.py will acquire data from the customers table from the telco_churn database\
on the codeup data science database server. You will want to join some tables as part of your query.
This data should end up in a pandas data frame.

Notebook

run acquire.py
summarize data (.info(), .describe(), .value_counts(), ...)
plot distributions of individual variables
'''

import pandas as pd
import numpy as np
import env

def get_db_url(database_name):
    return f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database_name}'

def get_telco_data():
    query = '''
    Select * FROM customers
    JOIN contract_types USING(contract_type_id)
    JOIN payment_types USING(payment_type_id)
    JOIN internet_service_types USING(internet_service_type_id);
    '''

    df = pd.read_sql(query, get_db_url('telco_churn'))
    return df 