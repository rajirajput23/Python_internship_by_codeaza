import json
from json import dump
from json import dumps
from requests import get

#json.loads

data= '{"name":"jr NTR", "age":28}'

parsed=json.loads(data)
print(parsed)
print(parsed['name'])

# json.load
#Creating json file

data1 = {
    "name": "Satyam kumar",
    "place": "patna",
    "skills": [
        "Raspberry pi",
        "Machine Learning",
        "Web Development"
    ],
    "email": "xyz@gmail.com",
    "projects": [
        "Python Data Mining",
        "Python Data Science"
    ]
}

#dump
with open( "data_file.json" , "w" ) as write:
    json.dump( data , write )

#After creating json file lets now load file   

with open("data_file.json", "r") as read_content:
    print(json.load(read_content))


