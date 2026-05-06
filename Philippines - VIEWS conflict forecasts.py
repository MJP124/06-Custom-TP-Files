import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'phl-views-conflict-forecasts-country-month.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))
sns.histplot(df['main_mean'].dropna(), kde=True, color='skyblue', bins=10)

plt.title('Distribution of Predicted Conflict Fatalities (main_mean)', fontsize=14)
plt.xlabel('Predicted Fatalities (main_mean)', fontsize=12)
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)

plt.show()