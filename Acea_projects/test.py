import pandas as pd
import glob
import os
import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")  # this is the regex expression to search on

# setting the path for joining multiple files
files = os.path.join("/Users/Flavio/Desktop/python_piscine/Acea_projects/", "*.csv")

# list of merged files returned
files = glob.glob(files)

print("Resultant CSV after joining all CSV files at a particular location...");

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)

# check with re instead and use drop to clean the csv based on multiple conditions
#jdf = df.drop(df[(df.score < 50) & (df.score > 20)].index)

print(df.to_string)


# df = pd.DataFrame({'email': ['firstname@domain.com', 'avicii@heaven.com', 'this.is.a.dot@email.com', 'email1234@112.com', 'notanemail'], 'euro': [123, 321, 150, 0, 133]})
# df['isemail'] = df['email'].apply(lambda x: True if pattern.match(x) else False)