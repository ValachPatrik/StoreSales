import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import cross_val_score

#%matplotlib inline 

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
holiday = pd.read_csv("holidays_events.csv")
stores = pd.read_csv("stores.csv")
oil = pd.read_csv("oil.csv")
transactions = pd.read_csv("transactions.csv")

#print(train.head())

data = pd.concat([train,test])
data = data.merge(holiday, "left", ["date"]).rename(columns={"type" : "holiday_type"})
data = data.merge(stores, "left", ["store_nbr"]).rename(columns={'type':'city_type'})
data = data.merge(transactions, "left", ["store_nbr", "date"])
data = data.merge(oil, "left", ["date"])

print(data.columns)