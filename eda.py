
import pandas as pd
data = pd.read_csv(r"C:\Users\pc\Desktop\Data science\MISSING_DATASET_HANDLING.csv",encoding='latin1')
print(data.isnull().sum())


#DROP

data = data.drop(columns=['ADDRESSLINE2'])
print(data.isnull().sum())

#if missing values are less we can drop the rows
data = data.dropna(subset=['ORDERDATE','PRODUCTLINE'])
print(data.isnull().sum())


#FILLING MISSING VALUES
data["MSRP"] = data["MSRP"].fillna(data["MSRP"].median())
data["YEAR_ID "] = data["YEAR_ID"].fillna(data["YEAR_ID"].mode()[0])
print(data.isnull().sum())
