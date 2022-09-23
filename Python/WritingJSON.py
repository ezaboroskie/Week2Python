#Writing JSON

#JSON value can be
#int, float, bool, dictionary, array
#array of int, array of dictionary, array of bool, etc

#importing json module so we can write json to a file

import json 

#writing JSON

with open("car.json" , "w") as file:  #"file" being a variable
    car = {"make": "Honda", "model": "Accord"}
    
    #json.dump(Object you want to write, File object)
    json.dump(car , file)  #"file" variable used as object


import json

with open ("person.json" , "w") as file:
  person_name = input("Enter your name: ")
  person_age = input("Enter you age: ")

  personName = {"name": person_name , "age" : person_age}
  json.dump(personName, file)


users=[]

while True:
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    user = {"name": user_name, "age" : user_age}
    users.append(user)
    choice = input("Q to quit or any key to continue: ")
    if choice == "q":
      break
  
with open ("users.json" , "w") as file: 
  json.dump(users, file)