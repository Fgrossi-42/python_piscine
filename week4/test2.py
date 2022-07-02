import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("atlcrime.csv")
choice = data["npu"].unique()
print(choice)