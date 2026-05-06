import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_name = "Power Generation by Fuel Source.csv"
try:
    df = pd.read_csv(file_name, encoding='utf-16', sep='\t')
except Exception:
    df = pd.read_csv(file_name)

df.columns = df.columns.str.strip()

numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

if numeric_cols:
    target_column = numeric_cols[0]
    
  
    plt.figure(figsize=(12, 6))
    sns.set_style("whitegrid")
    
    sns.histplot(df[target_column].dropna(), bins=15, kde=True, color='royalblue')
    
    plt.title(f'Distribution of Power Generation: {target_column}', fontsize=15)
    plt.xlabel('Generation Value', fontsize=12)
    plt.ylabel('Frequency (Count)', fontsize=12)
    
    plt.tight_layout()
    plt.show()
else:
    print("Error: No numerical columns found in the CSV file.")