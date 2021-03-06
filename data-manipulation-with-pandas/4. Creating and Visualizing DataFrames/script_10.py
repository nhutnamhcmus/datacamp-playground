import pandas as pd 

temperatures = pd.read_csv('../datasets/temperatures.csv')

# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country', 'city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [('Brazil', 'Rio De Janeiro'), ('Pakistan', 'Lahore')]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Add a year column to temperatures
temperatures["date"] = pd.to_datetime(temperatures["date"], errors='coerce')
temperatures["year"] = temperatures["date"].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table("avg_temp_c", index = ["country", "city"], columns = "year")

# See the result
print(temp_by_country_city_vs_year)

# Subset for Egypt to India
print(temp_by_country_city_vs_year.loc['Egypt':'India'])

# Subset for Egypt, Cairo to India, Delhi
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'): ('India', 'Delhi')])

# Subset in both directions at once
print(temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'): ('India', 'Delhi'), '2005': '2010'])