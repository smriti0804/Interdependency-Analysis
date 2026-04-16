import matplotlib.pyplot as plt
import pandas as pd
a=pd.read_excel("/merged data.xlsx")
df=pd.DataFrame(a)
corrMatrix=a.corr()
print("correlation Matrix= ",corrMatrix)
