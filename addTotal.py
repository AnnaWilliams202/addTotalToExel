import pandas as pd

data_files = pd.read_excel('input.xlsx')
print(data_files.head())
print(data_files.info())
print(data_files.__dataframe__())

data_files['Total'] = data_files['Price']*data_files['Quantity']
data_files.to_excel('output.xlsx', index=False)

output = pd.read_excel('output.xlsx')
print(output.head())