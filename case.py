#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
df = df.dropna()

print('Среди топ 5 самых населенных стран преимущетвенно находяься в Азии')
sorted_df = df.sort_values(by='Population')
top_5_countries_of_pop = sorted_df.tail(5)
top_5_countries_of_pop['Population'].value_counts().plot(kind = 'barh', figsize = (8, 5))
print(top_5_countries_of_pop)
plt.show()
