#место для твоего кода
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('countries of the world.csv')
df = df.dropna()
#df.info()

# temp = df['Region'].value_counts()
# print(temp.keys())

# countries_asia = df[df['Region']=='ASIA (EX. NEAR EAST)         ']
# countries_w_europe = df[df['Region']=='WESTERN EUROPE                     ']
# countries_e_europe = df[df['Region']=='EASTERN EUROPE                     ']
# countries_n_africa = df[df['Region']=='NORTHERN AFRICA                    ']
# countries_n_america = df[df['Region']=='NORTHERN AMERICA                   ']
# countries_baltics = df[df['Region']=='BALTICS                            ']
# countries_ = df[df['Region']=='C.W. OF IND. STATES ']
# print(countries_)

print('Среди топ 5 самых населенных стран преимущетвенно находяься в Азии')
sorted_df = df.sort_values(by='Population')
top_5_countries_of_pop = sorted_df.tail(5)
top_5_countries_of_pop['Population'].value_counts().plot(kind = 'barh', figsize = (8, 5))