import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('weather.csv')
data = df['wind_kmh'].dropna()

# Настройка холста (1 строка, 2 колонки)
sns.set_theme(style="whitegrid") #Here i make for him theme white 
fig, axes = plt.subplots(1, 2, figsize=(12, 5)) # 1 stroke and 2 colomn 

# График 1: Гистограмма (показывает форму распределения)
sns.histplot(data, kde=True, ax=axes[0], color='#3498db', alpha=0.6)
axes[0].axvline(data.mean(), color='#e74c3c', linestyle='--', linewidth=2, label=f'Mean: {data.mean():.2f}')
axes[0].axvline(data.median(), color='#2ecc71', linestyle='-', linewidth=2, label=f'Median: {data.median():.2f}')
axes[0].set_title('Distribution & Central Tendency')
axes[0].legend()

# График 2: Boxplot (визуализация IQR, Медианы и выбросов)
sns.boxplot(x=data, ax=axes[1], color='#95a5a6')
axes[1].set_title('Boxplot: IQR and Outliers')

plt.tight_layout()
plt.show()