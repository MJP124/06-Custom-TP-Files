import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "Local Inventory of Cultural Property (TALAPAMANA).xls"
try:

    df = pd.read_excel(file_name, sheet_name='TALAPAMANA')
except Exception:

    df = pd.read_excel(file_name)

df.columns = df.columns.str.strip()

plt.figure(figsize=(10, 6))
sns.set_style("whitegrid")

plot = sns.countplot(data=df, x='URI', palette='magma', hue='URI', legend=False)

# Add Titles and Labels
plt.title('Distribution of Local Cultural Properties by Type', fontsize=15)
plt.xlabel('Property Category (URI)', fontsize=12)
plt.ylabel('Total Count', fontsize=12)

for p in plot.patches:
    plot.annotate(f'{int(p.get_height())}', 
                  (p.get_x() + p.get_width() / 2., p.get_height()), 
                  ha='center', va='center', xytext=(0, 9), 
                  textcoords='offset points')

plt.tight_layout()
plt.show()