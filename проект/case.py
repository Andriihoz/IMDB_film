import pandas as pd

df = pd.read_csv('IMDB-Movie-Data.csv')

df.info()
#місце для твого коду
score = df['Reating score'].mean()
print('score')