'''
Data Prep
Prepare.py

split data to train/test
Handle Missing Values
Handle erroneous data and/or outliers you wish to address
encode variables as needed
scale data as needed
new feature that represents tenure in years (code in notebook)
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

def split_my_data_csv(df):
    X = df.drop(columns = ["churn"])
    y = df[['churn']]
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .80, random_state = 123)
    return X, y, X_train, X_test, y_train, y_test

def encoder_all(df):
    encoder = LabelEncoder()
    df_encoded = df.drop(columns=['contract_type', 'internet_service_type','payment_type'])
    encode_list = ['gender','partner', 'dependents', 'phone_service','multiple_lines', 'online_security', \
                  'online_backup','device_protection','tech_support','streaming_tv', \
                  'streaming_movies', 'paperless_billing', 'churn']
    for c in encode_list:
        df_encoded[c] = encoder.fit_transform(df_encoded[c])
    return df_encoded

def encoder_all_rf(df):
    encoder = LabelEncoder()
    df_encoded_rf = df.drop(columns=['contract_type', 'internet_service_type','payment_type','gender','phone_service','streaming_movies','tech_support'])
    encode_list = ['partner', 'dependents','multiple_lines', 'online_security', \
                  'online_backup','device_protection','streaming_tv', \
                  'paperless_billing', 'churn']
    for c in encode_list:
        df_encoded_rf[c] = encoder.fit_transform(df_encoded_rf[c])
    return df_encoded_rf