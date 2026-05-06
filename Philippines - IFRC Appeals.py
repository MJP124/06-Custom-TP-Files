import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'appeals_data_phl.csv'
df = pd.read_csv(file_path)

df['amount_requested'] = pd.to_numeric(df['amount_requested'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df['amount_requested'].dropna(), kde=True, color='skyblue', bins=30)

plt.title('Distribution of Amount Requested for Appeals (Philippines)')
plt.xlabel('Amount Requested (CHF)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = 'appeals_data_phl.csv'
df = pd.read_csv(file_path)

df['amount_requested'] = pd.to_numeric(df['amount_requested'], errors='coerce')

plt.figure(figsize=(10, 6))
sns.histplot(df['amount_requested'].dropna(), kde=True, color='skyblue', bins=30)

plt.title('Distribution of Amount Requested for Appeals (Philippines)')
plt.xlabel('Amount Requested (CHF)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)

plt.show()