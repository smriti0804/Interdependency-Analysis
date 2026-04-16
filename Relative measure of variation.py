import pandas as pd
import numpy as np
from sympy import *
a=pd.read_excel("/content/mergedsurat data.xlsx")
df=pd.DataFrame(a)
cm=df.cov()
print("covariance matrix=",cm.round(3))
C=Matrix(cm)
p,d=C.diagonalize()
print("Diagonalized matrix : {}".format(d))
D=np.diag(d)
print("Diagonal elements=",D)
t=np.trace(d)
print("Trace=",t)
R=list(map(lambda D:D/t,D))
print("R=",R)
