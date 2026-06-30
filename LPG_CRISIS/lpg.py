import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r"C:\Users\Deekshitha C\OneDrive\ドキュメント\India_lpg_dataset.csv")
df = df[['Year', 'Production_MMT', 'Consumption_MMT', 'Price_INR']]
df.columns = ['Year', 'Production', 'Consumption', 'Price']
print(df.head())
print(df.describe())
sns.barplot(x='Year', y='Price', data=df,hue="Year")
plt.xticks(rotation=45)
plt.show()