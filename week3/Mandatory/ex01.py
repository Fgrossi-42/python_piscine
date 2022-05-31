import pandas as pd

df = pd.read_csv('Salaries.csv')

df.info(verbose = False, memory_usage = False)
