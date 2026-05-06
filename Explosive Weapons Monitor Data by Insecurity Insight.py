import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '2020-2026-explosive-weapons-incident-data.xlsx'
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

df['Health Infrastructure Damaged/Destroyed'] = pd.to_numeric(df['Health Infrastructure Damaged/Destroyed'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df['Health Infrastructure Damaged/Destroyed'].dropna(), kde=False, color='skyblue', bins=10)

plt.title('Distribution of Health Infrastructure Damaged/Destroyed')
plt.xlabel('Incidents of Damage/Destruction')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '2020-2026-explosive-weapons-incident-data.xlsx'
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

df['Health Infrastructure Damaged/Destroyed'] = pd.to_numeric(df['Health Infrastructure Damaged/Destroyed'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df['Health Infrastructure Damaged/Destroyed'].dropna(), kde=False, color='skyblue', bins=10)

plt.title('Distribution of Health Infrastructure Damaged/Destroyed')
plt.xlabel('Incidents of Damage/Destruction')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)

plt.show()