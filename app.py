import pandas as pd

netflix = pd.read_csv('netflix_titles.csv')

# print(netflix.tail())
# print(len(netflix))
# print(netflix.dtypes)
# print(netflix.filter('release_year' < 2018))
# print(netflix.shape)

# You get a sereis
# print(netflix.iloc[2])
# print(netflix.iloc[:3,3])
# print(netflix.iloc[-5:,-3])

# You get the direct value
# print(netflix.iloc[:3,2])

# Using loc
# print(netflix.loc[:3,'title'])

# conditional selecting
# print(netflix.loc[(netflix.release_year == 2020) & (netflix.type == 'Movie')])
# print(netflix.loc[netflix.release_year.isin([2021])])

# print(netflix.loc[netflix.director.notnull()])

# Get all columns
# print(netflix.columns)

# Describe a particular column
# print(netflix.country.describe())

# Find out all unique values
# print(netflix.country.unique())

# Count of individual values in a column
print(netflix.rating.value_counts())

