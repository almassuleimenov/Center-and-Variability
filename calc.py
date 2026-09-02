import pandas as pd

df = pd.read_csv('weather.csv')

data = df['wind_kmh'].dropna()

print(f"Sample Size (N): {len(data)}")
print(f"Mean: {data.mean():.2f}")
print(f"Median: {data.median():.2f}")
print(f"Variance: {data.var(ddof=1):.2f}")
print(f"Standard Deviation: {data.std(ddof=1):.2f}")
print(f"Range: {data.max() - data.min():.2f}")
print(f"IQR: {data.quantile(0.75) - data.quantile(0.25):.2f}")