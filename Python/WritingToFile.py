#writing to a file

#open(name of file, mode) default mode is "r"

# w = writing a file
# r = reading a file (default)
# a = appending a file

#opening the file for writing, create a file if it does not exist 

# file=open("todo.txt", "w")
    #write text to a file
# file.write("mow the lawn")
    #ALWAYS close the file
# file.close()

userName=input("Enter your name: ")
file=open("Name.txt", "w")
file.write(userName)
file.close()

#PREFERED METHOD (DOES NOT REQUIRE .close())
# with open("todo.txt", "w") as file:
#\n writes on new line

with open("todo.txt", "w") as file:
    file.write("Make dinner")  #will be written on one line
    file.write("Do Homework")  # "           "
    file.write("Exercise")     # "           "
    file.write("Clean car \n")
    file.write("Mow the lawn \n")
    file.write("Mail envelopes")

#Appending a file 
while True:
    task_name = input("Enter task or press q to quit: ")

    if task_name == "q":
        break

    with open("todo.txt", "a") as file:
        file.write(task_name)
        file.write("\n")  #appends task to new line

#Reading a file
with open("todo.txt") as file:
    print(file.read())
    #can create variable to read from 
    content = file.read()
print(content)
