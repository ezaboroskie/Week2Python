import json

with open("users.json") as file:
    #get back array of dictionaries since you wrote to json an array of dicitonaries
    #json.load can only load VALID json documents
    result = json.load(file)

print(result)