import pandas as pd
import numpy as np
import pickle

data= pd.read_csv('Characters.csv',encoding= 'unicode_escape')
data.set_index('Name',inplace=True)
print(data.head(5))
pickle.dump(data,open("harry.pkl",'wb'))