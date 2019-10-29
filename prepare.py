'''
Data Prep
Prepare.py

split data to train/test
Handle Missing Values
Handle erroneous data and/or outliers you wish to address
encode variables as needed
scale data as needed
new feature that represents tenure in years
create single variable representing the information from phone_service and multiple_lines
do the same using dependents and partner
other ways to merge variables, such as streaming_tv & streaming_movies, online_security & online_backup
'''

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import env
import acquire
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer,RobustScaler,MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler


def clean_data(df):
    df = df[df.total_charges != ' ']
    df.total_charges = df.total_charges.astype(float)
    return df

def wrangle_telco():
    df = get_data_from_mysql()
    df = clean_data(df)
    return df


def encoder(df):
    encoder = LabelEncoder()
    encoder.fit(df.churn)
    df.churn = encoder.transform(df.churn)
    return df

def split_my_data(df):
    X = df.drop(columns = 'churn')
    y = df[['churn']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .80, random_state = 123)
    return X, y, X_train, X_test, y_train, y_test

def split_my_data_bl(df):
    X = df[['internet_service_type_id', 'payment_type_id', 'contract_type_id', 'senior_citizen', 'tenure', 'monthly_charges', 'total_charges']]
    y = df[['churn']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .80, random_state = 123)
    return X, y, X_train, X_test, y_train, y_test



def prep_telco_data(data):
    encoder = LabelEncoder()
    data = data.drop(columns=['contract_type', 'internet_service_type','payment_type'])
    data['total_charges'] = pd.to_numeric(data['total_charges'],errors='coerce')
    encode_list = ['gender','partner', 'dependents', 'phone_service','multiple_lines', 'online_security', 'online_backup','device_protection','tech_support','streaming_tv', \
                  'streaming_movies', 'paperless_billing', 'churn']
    for c in encode_list:
        data[c] = encoder.fit_transform(data[c])
    return data