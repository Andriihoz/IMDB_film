import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('IMDB-Movie-Data.csv')

#місце для твого коду


df.plot(x = 'Rating',y = 'Votes',kind ='hist')
plt.xlabel('Оцінки')
plt.ylabel('Кількість фільмів')
plt.title('Гістограма оцінок фільмів на IMDb')
plt.show()