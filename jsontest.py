import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to test.json
with open("test.json", "w") as outfile:
    outfile.write(json_object)
    
# Opening JSON file
with open("test.json", "r") as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object["name"])

for i in range(4):
    name = input("Enter name: ")
    rollno = input("Enter rollno: ")
    
    dictionary[name] = rollno
    
print(dictionary)