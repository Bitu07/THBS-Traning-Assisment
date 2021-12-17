import json
people_string ='''
{
    "people":[
    {
        "name":Harsh Kumar",
        "phone::"2324556",
        "email":["h@gmail.com","h1@gmail.com"]
        "has_license":false
    },
    {
        "name":Bhaggu Tiwari",
        "phone::"2323434",
        "email":null,
        "has_license":true
    }
    ]
    }
    '''
data = json.loads(people_string)
# print(type(data))
# print(data)
# for person in data["people"]:
#     print(person['name'])
for person in data["people"]:
    del person['phone']
new_json = json.dumps(data,indent=2)
# new_json = json.dumps(data)
print(new_json)