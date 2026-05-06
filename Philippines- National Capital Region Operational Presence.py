import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'FieldsData_3W_PHL_NCR.xlsx'
df = pd.read_excel(file_path)

df = df.drop(df.index[0])

sector_counts = df['Sector'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=sector_counts.index, y=sector_counts.values, palette='viridis')

plt.title('Distribution of Humanitarian Activities by Sector (NCR, Philippines)')
plt.xlabel('Sector')
plt.ylabel('Number of Activities')
plt.xticks(rotation=45, ha='right')


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'FieldsData_3W_PHL_NCR.xlsx'
df = pd.read_excel(file_path)

df = df.drop(df.index[0])

sector_counts = df['Sector'].value_counts()

plt.figure(figsize=(10, 6))
sns.barplot(x=sector_counts.index, y=sector_counts.values, palette='viridis')

plt.title('Distribution of Humanitarian Activities by Sector (NCR, Philippines)')
plt.xlabel('Sector')
plt.ylabel('Number of Activities')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()