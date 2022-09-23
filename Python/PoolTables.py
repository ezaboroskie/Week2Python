
from datetime import datetime


Tables = []

#Classes

class PoolTable:
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        self.isOccupied = False
        self.startTime = None
        self.endTime = None
    
    def check_out(self):
        table = self.isOccupied
        if table == True:
            print("")
            print("!!!!This table is currently in use!!!!")
            print("")
        else:
            self.isOccupied = True
            self.startTime = datetime.now()

    def check_in(self):
        self.isOccupied = False
        self.endTime = datetime.now()    
        
for index in range(1 , 13):
    pool_table = PoolTable(index)
    Tables.append(pool_table)


#Main Menu

print("")
print("------Welcome to the Pool Table Manager------")
print("")
print("---Please select from the following options---")
print("")

while True: 
    print("---------------------")
    print("1. Add Players to a Table")
    print("")
    print("2. End a Table Session")
    print("")
    print("3. View All Tables' Status")
    print("---------------------")
    print("")

    range_0 = range(1, 4, 1)
    range_1 = range(1, 13, 1)

    choice = input("Enter a number from the menu or q to quit: ")
    print("")

    if choice in range_0:
        print("")
    
        

#Choice 1: Check Out a Table

    elif choice == "1":
        for pt in Tables:
            print(f"{pt.tableNumber} - Is Occupied: {pt.isOccupied} - Start Time: {pt.startTime} - End Time: {pt.endTime}")
            print("")
        table_number_check_out = int(input("Enter the table number to add players: "))
        print("")
        if table_number_check_out in range_1:
            pool_table = Tables[table_number_check_out - 1]
            pool_table.check_out()
        else:
            print("")
            print("!!!!!! Enter a Valid Pool Table Number (1-12) !!!!!!")
            print("")
        
 #Choice 2: Check In a Table
    
    elif choice == "2":
        for pt in Tables:
            print(f"{pt.tableNumber} - Is Occupied: {pt.isOccupied} - Start Time: {pt.startTime} - End Time: {pt.endTime}")
            print("")
        table_number_check_in = int(input("Enter the table number to open table: "))
        print("")
        if table_number_check_in in range_1:
            pool_table = Tables[table_number_check_in - 1]
            pool_table.check_in()
        else:
            print("")
            print("!!!!!! Enter a Valid Pool Table Number (1-12) !!!!!!")
            print("")

        current_date_and_time = datetime.now()
        current_date_and_time_string = str(current_date_and_time)
        extension=".txt"
        file_name = current_date_and_time_string + extension

        with open(file_name , "a") as file:
          file.write(f"{table_number_check_in} \n") 
          file.write(f"{pool_table.startTime} \n")
          file.write(f"{pool_table.endTime} \n")
          file.write(f"{pool_table.endTime - pool_table.startTime} \n")


#Choice 3: View All Tables
 
    elif choice == "3":
        for pt in Tables:
            print(f"{pt.tableNumber} - Is Occupied: {pt.isOccupied} - Start Time: {pt.startTime} - End Time: {pt.endTime}")

    elif choice == "q":
        break

#Error message for incorrect menu selection
    else:
        print("")
        print("!!!!!!Please Select a Valid Menu Option (1 - 3)!!!!!!")
        print("")
    