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