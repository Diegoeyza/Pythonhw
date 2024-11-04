import matplotlib.pyplot as plt
import pandas as pd

# Load CSV data into a DataFrame
file_path = r"C:\Users\diego\Downloads\e3 eda results - queries.csv"
df = pd.read_csv(file_path)

# Set the x-axis (file names) and use the first row as the tree labels
file_names = df.iloc[:, 0]
tree_labels = df.columns[2:3]  # Ignore the first column 'Files/Trees'

# Plot each tree's creation times with file names on the x-axis
plt.figure(figsize=(10, 6))
for tree in tree_labels:
    # Select only non-missing values for both x (file_names) and y (tree times)
    valid_data = df[[df.columns[0], tree]].dropna()
    plt.plot(valid_data[df.columns[0]], valid_data[tree]*(10**-3), label=tree, marker='o')

# Set plot title and labels
plt.title('Tree Creation Times for Different Files')
plt.xlabel('Files')
plt.ylabel('Time to Create Tree (milliseconds)')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
