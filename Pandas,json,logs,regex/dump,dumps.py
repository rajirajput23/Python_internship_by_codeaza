from json import dump
from json import dumps
from requests import get


responseObject = get('http://api.open-notify.org/astros.json')
print(responseObject)
print()

jsonData= responseObject.json()
print(jsonData)

jsonStringData=dumps(jsonData)

with open('issAstrosDumps.json','w')as f:
    print("now writing into filee....")
    print()
    f.write(jsonStringData)

jsonOutputFile=open('isAstroDump.json','w')
dump(jsonData,jsonOutputFile,indent= 4)