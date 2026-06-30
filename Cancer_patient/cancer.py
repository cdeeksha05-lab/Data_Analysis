import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read dataset
data = pd.read_csv("dataset\\india_cancer_patients_2022_2025.csv")
print(data)

print(data.head())
print(data.tail())


df = data[['Patient_ID','State','Cancer_Type','Stage','Treatment_Type','Status']]
df.columns = ['Id','St','Type','Stage','Treat','Stat']

print(df)
state = df.groupby(['St','Stat']).size().reset_index(name='Total')

print(state)

plt.figure(figsize=(12,6))
sns.barplot(x='St', y='Total', hue='Stat', data=state)

plt.title("State-wise Cancer Patient Status")
plt.show()

dead = df[df['Stat'] == 'Deceased']
reason = dead.groupby(['St','Stage']).size().reset_index(name='Total')
print(reason)

plt.figure(figsize=(12,6))

sns.barplot(x='St', y='Total', hue='Stage', data=reason)

plt.title("State-wise Cancer Stage of Deceased Patients")
plt.show()