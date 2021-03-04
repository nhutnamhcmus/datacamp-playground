# Import pandas using the alias pd
import pandas as pd

homelessness = pd.read_csv('datasets/homelessness.csv')

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)