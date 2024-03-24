import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the CSV file
df = pd.read_csv('data.csv', index_col=1)

# Identify the most common numbers
mode = stats.mode(df)

# Generate a plot highlighting these numbers
plt.figure(figsize=(10,6))
sns.heatmap(df == mode.mode[0], cmap='Reds')

# Save the plot as an image
plt.savefig('heatmap.png')