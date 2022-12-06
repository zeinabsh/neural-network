import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

filepath = "penguins.csv"
df = pd.read_csv(filepath)
#Data Preprocessing
#Removing null values
df['gender'].fillna('male', inplace=True)
#male replaced with 1
df['gender'].replace('male', 1,inplace=True)
#female replaced with 0
df['gender'].replace('female', 0,inplace=True)


df_Adelie    = df[df['species'] == 'Adelie']
df_Gentoo    = df[df['species'] == 'Gentoo']
df_Chinstrap = df[df['species'] == 'Chinstrap']

print(df.info())

feature1 = 'bill_length_mm'
feature2 = 'bill_depth_mm'
feature3 = 'flipper_length_mm'
feature4 = 'gender'
feature5 = 'body_mass_g'

df['species'].replace('Adelie'   , 1 , inplace=True)
df['species'].replace('Gentoo'   , -1, inplace=True)
df['species'].replace('Chinstrap', 2 , inplace=True)

# normalized data
columns = ['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','gender']
for column in columns:
  df[column] = MinMaxScaler().fit_transform(np.array(df[column]).reshape(-1,1))


