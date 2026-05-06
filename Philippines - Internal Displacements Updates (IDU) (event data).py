import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'event_data_phl.csv'
df = pd.read_csv(file_path)

# Create a histogram of the 'figure' column (displacement figures)
plt.figure(figsize=(10, 6))
sns.histplot(df['figure'].dropna(), kde=True, color='skyblue', bins=20)

# Set titles and labels
plt.title('Distribution of Displacement Figures in the Philippines (2026)')
plt.xlabel('Displacement Figure')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)

# Display the plot
plt.show()