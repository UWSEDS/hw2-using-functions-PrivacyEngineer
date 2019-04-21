# Data 515, Software Engineering for Data Scientists
# Homework 2
# M.S. Data Science, University of Washington, Spr. 2019.
# Francisco Javier Salido Magos.

import requests
import io
import pandas as pd


def test_create_dataframe(newdf):
    """
    Compares a preselected dataframe to a new dataframe for similarity.
    
    The function takes a preselected dataframe (df) and compares it to a new
    dataframe (newdf), to see if a set of similarity conditions are met.
    Similarity conditions are:  a) The schema of newdf, its columns and column
    data types are the same as those of df, and b) If the number of rows in
    newdf is 10 or greater.  The only input parameter is newdf, but two global
    variables that describe df are also expected:  A LIST type variable
    (columns_df) containing the column names of df, listed in alphabetical
    order.  A LIST type variable (data_types_df) containing the data type for
    each column in df, listed in the same order as columns_df.  Output will be
    True if all conditions are met, and False otherwise.
    """

    # First compare the shape of newdf to see if it matches requirements.
    if(newdf.shape[0] >= 10 and newdf.shape[1] == len(columns_df)):
        # Sort newdf columns to compare column names and data types to df.
        newdf = newdf.reindex(sorted(newdf.columns), axis=1)
        if(list(newdf.columns) == columns_df and
                list(newdf.dtypes) == data_types_df):
            return True
        pass
        return False
    pass
    return False


# Read data from original online source and create dataframe from question 1.
url = ("http://data-seattlecitygis.opendata.arcgis.com/datasets/"
            "a2e1128bd7a041358ce455c628ec9834_8.csv")
req = requests.get(url)
assert req.status_code == 200
raw_df = pd.read_csv(io.StringIO(req.text))

# Creating dataframe (df) for question 1 from raw data downloaded from Seattle
#   city website.
df = raw_df[["X", "Y", "TYPE", "SCHOOL", "WEBSITE"]]
df = df.reindex(sorted(df.columns), axis=1)
# Extracting column names and data types.
columns_df = list(df.columns)
data_types_df = list(df.dtypes)

# Comparing the full (raw) dataframe downloaded from Seattle city website
#   and df.
if test_create_dataframe(raw_df):
    print("\nConditions hold\n")
else:
    print("Fail: Conditions do not hold\n")

# Comparing df to a subset of df.
if test_create_dataframe(df.iloc[:11]):
    print("Conditions hold\n")
else:
    print("Fail: Conditions do not hold\n")

# Comparing df to a subset of df, but the subset is too small.
if test_create_dataframe(df.iloc[:5]):
    print("Conditions hold\n")
else:
    print("Fail: Conditions do not hold\n")
