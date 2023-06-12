import pandas as pd

df = pd.DataFrame(columns=['ID','Name'])

dict_1 = {'ID':1, 'Name':'Jack'}
row_1 = pd.Series(dict_1)

df = pd.concat([df, row_1.to_frame().T], ignore_index= True)

df.set_index('ID', inplace=True)
df.to_excel("pdtest.xlsx") 
