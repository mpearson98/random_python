import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the CSV file
csv_path = 'path_to_your_csv.csv'

# Read the CSV file
df = pd.read_csv(csv_path)

# Format the DataFrame as needed
# For example, let's sort the DataFrame by the first column
df = df.sort_values(by=df.columns[0])

# Create a graph
# For example, let's create a line plot of the first two columns
plt.plot(df[df.columns[0]], df[df.columns[1]])

# Show the graph
plt.show()