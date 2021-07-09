import pandas as pd

frame = {'names':['Kev','Brian','Sam'], 'scores': [80,100,75]}
rframe = pd.DataFrame(data=frame)

#looping through for key will only give headers, 
# looping through values will give indexes and values

# for (key,value) in rframe.items():
#     print(key)

#this will give names and scores along with values in each column
for (index,row) in rframe.iterrows():
    print(row)