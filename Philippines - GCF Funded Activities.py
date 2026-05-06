import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'philippines-gcf-funded-activities.csv'
df = pd.read_csv(file_path)

df['FA Financing'] = pd.to_numeric(df['FA Financing'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df['FA Financing'].dropna(), kde=True, color='green', bins=10)

plt.title('Distribution of GCF Financing for Projects in the Philippines')
plt.xlabel('FA Financing (in USD)')
plt.ylabel('Number of Projects')
plt.grid(axis='y', alpha=0.3)

plt.show()