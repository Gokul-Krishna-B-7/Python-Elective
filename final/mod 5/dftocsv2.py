import pandas as pd

dict= {
    "name":['Reo','A','B','C','D'],
    'age':[1,2,3,4,5],
    'degree':['mba','mda','mda','mda','mda'],
    "score":[1,2,3,4,5],
}

fd=pd.DataFrame(dict)
print(fd)

fd.to_csv('data.csv')
gv=pd.read_csv('data.csv')
print(gv)