import pandas as pd

netflix = pd.read_csv('netflix_titles.csv')

# print(netflix.tail())
print(len(netflix))
# print(netflix.dtypes)
print(netflix.filter('release_year' < 2018))