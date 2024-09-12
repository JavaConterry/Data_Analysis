import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')

print(df.info())
print(df.describe())

int_cols = ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak', 'HeartDisease']
df = df.drop(df.loc[df['Cholesterol'] == 0].index)
df = df.reset_index(drop=True)

plt.plot(df[int_cols])
plt.legend(int_cols)
plt.show()

print(df.info())
print(df.describe())

df.to_csv('heart_preprocessed.csv')