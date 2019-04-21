"""
Data 515, Software Engineering for Data Scientists
Homework 2
M.S. Data Science, University of Washington, Spr. 2019.
Francisco Javier Salido Magos.
"""
import requests
import io
import pandas as pd


"""
Test the original dataframe to the new dataframe decide if it is similar.
Similarity test returns True if the schema of new dataframe (columns
and data types) is the same as that of the original, and if the number
of rows in the new dataframe is 10 or greater. The only parameter is
newdf, the new dataframe.
"""


def test_create_dataframe(newdf):
    if(newdf.shape[0] >= 10 and newdf.shape[1] == len(columns_df)):
        newdf = newdf.reindex(sorted(newdf.columns), axis=1)
        if(list(newdf.columns) == columns_df and
                list(newdf.dtypes) == data_types_df):
            return True
        pass
        return False
    pass


# Read data from original online source and create dataframe from question 1.
url = "http://data-seattlecitygis.opendata.arcgis.com/datasets/a2e1128bd7a041358ce455c628ec9834_8.csv"
req = requests.get(url)
assert req.status_code == 200
raw_df = pd.read_csv(io.StringIO(req.text))

# Creating dataframe for question 1 from raw data downloaded from Seattle
# city website.
df = raw_df[["X", "Y", "TYPE", "SCHOOL", "WEBSITE"]]
df = df.reindex(sorted(df.columns), axis=1)
columns_df = list(df.columns)
data_types_df = list(df.dtypes)

# Comparing the original (raw) dataframe and the new one.
if test_create_dataframe(raw_df):
    print("Conditions hold\n")
else:
    print("Fail: Conditions do not hold\n")
# Comparing two versions of the original dataframe.
if test_create_dataframe(df.iloc[:11]):
    print("Conditions hold\n")
else:
    print("Fail: Conditions do not hold\n")
# Comparing two versions of the original dataframe, but the copy is too small.
if test_create_dataframe(df.iloc[:5]):
    print("Conditions hold\n")
else:
    print("Fail: Conditions do not hold\n")
