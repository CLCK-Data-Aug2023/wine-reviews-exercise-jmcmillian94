# add your code here
import pandas as pd 
import zipfile

#read in zipped csv
with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
    csv_filename = zip_ref.namelist()[0]
    df = pd.read_csv(zip_ref.open(csv_filename))
print(df)

# Group by 'country' and calculate the count and mean of the 'points' column
country_stats = df.groupby('country')['points'].agg(['count', 'mean']).reset_index()

# Rename the columns for clarity
country_stats.columns = ['Country', 'Count', 'Points']

#write file to csv in data folder
country_stats.to_csv('data/reviews-per-country.csv', sep=',', index=False)