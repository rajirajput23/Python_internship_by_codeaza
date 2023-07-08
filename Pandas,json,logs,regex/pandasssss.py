import numpy as np
import pandas as pd


dict1={

    "name":['harry', "jerry",'george', 'sam'],
    "marks":[70,50,85,65],
    "city":['islamabad','lahore','karachi','Faislabad']

}
dict2={

    "brands":['lambo', "mercedes",'audi', 'ferrari'],
    "prices":[7000000,2500000,5000000,13000000],
    "nations":['itly','Germany','france','spain']
}

df=pd.DataFrame(dict1)
print(df)

df1=pd.DataFrame(dict2)
print(df)



#locate row
print(df.loc[0])

#locate rows 0 and 1
print(df.loc[[0, 1]])


#Series
a=[1,4,5]
myvar = pd.Series(a)
print(myvar)

#labels
print(myvar[0])

#Creating own labels
myvar = pd.Series(a, index = ["x", "y", "z"])


#Reshaping Data

pd.melt(df)
df.pivot

#append rows of dataframe
pd.concat([df,df1])

#Append columns of dataframe
pd.concat([df,df1],axis=1)

# Sorting dataframe
df.sort_index()


#converting Dataframe to csv files
df.to_csv('friends.csv')
df1.to_csv('Cars.csv')
