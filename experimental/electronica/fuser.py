import pandas as pd

# Load the two CSV files into dataframes
df1 = pd.read_csv(r'experimental\electronica\channel_1.CSV')
df2 = pd.read_csv(r'experimental\electronica\channel_2.CSV')

# Select specific columns to keep from each dataframe
df1_selected = df1[['Source', 'CH1']]  # Replace with the columns you want from df1

# Ensure df2's 'CH1' is treated as numeric and multiply starting from row 2
df2['CH1'] = pd.to_numeric(df2['CH1'], errors='coerce')  # Convert to numeric if necessary
df2.loc[1:, 'CH1'] = df2.loc[1:, 'CH1'] * 1300

# Select the modified column from df2
df2_selected = df2[['CH1']]

# Concatenate the dataframes horizontally (axis=1 means columns-wise)
df_fused = pd.concat([df1_selected, df2_selected], axis=1)

# Save the fused dataframe into a new CSV file
df_fused.to_csv('fused_file.csv', index=False)

print("CSV files successfully fused and saved as 'fused_file.csv'")
