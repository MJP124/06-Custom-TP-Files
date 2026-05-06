import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "COR-Debt-Service_Monthly_1986-2024.xlsx"

df = pd.read_excel(file_name, sheet_name='2024', skiprows=4)

df.columns = [str(c).strip() for c in df.columns]
df['Total'] = pd.to_numeric(df['Total'], errors='coerce')

plot_data = df['Total'].dropna()
plot_data = plot_data[plot_data > 0]

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

sns.histplot(plot_data, bins=15, kde=True, color='darkred')

plt.title('Distribution of Monthly Debt Service Totals (2024)', fontsize=14)
plt.xlabel('Amount (In Million Pesos)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.tight_layout()
plt.show()