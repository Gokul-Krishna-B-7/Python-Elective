import pandas as pd
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# print(sdata)
obj3=pd.Series(sdata)
# print(obj3)
arr = [7,34,201,10]
# print(arr)
obj2 = pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)