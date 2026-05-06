import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'phl_co2e_20yr_city.csv'
df = pd.read_csv(file_path)

df['emissionsQuantity'] = pd.to_numeric(df['emissionsQuantity'], errors='coerce')

summary_stats = df['emissionsQuantity'].describe()
print("Summary Statistics for Emissions:")
print(summary_stats)

yearly_emissions = df.groupby('year')['emissionsQuantity'].sum().reset_index()
print("\nYearly Emissions Totals:")
print(yearly_emissions)


plt.figure(figsize=(10, 6))
sns.histplot(df['emissionsQuantity'].dropna(), kde=True, color='skyblue', bins=30)
plt.title('Distribution of CO2e Emissions across Philippine Cities')
plt.xlabel('Emissions Quantity (CO2e)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.savefig('emissions_histogram.png')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=yearly_emissions, x='year', y='emissionsQuantity', marker='o', color='green')
plt.title('Total CO2e Emissions Trend (2024-2026)')
plt.xlabel('Year')
plt.ylabel('Total Emissions (CO2e)')
plt.xticks(yearly_emissions['year'])
plt.grid(True, linestyle='--', alpha=0.7)
plt.savefig('yearly_emissions_trend.png')
plt.show()