#importing date and time functions

from datetime import datetime


#Creating an Empty Array

Tables = []


#Classes

class PoolTable:
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        self.isOccupied = False
        self.startTime = None
        self.endTime = None
    
    def check_out(self):
        now = datetime.now()
        time_string = now.strftime("%I:%M:%S")
        table = self.isOccupied
        if table == True:
            print("================================================")
            print("|                   !ERROR!                    |")
            print("|==============================================|")
            print("|    !!!!This table is currently in use!!!!    |")
            print("================================================")
        else:
            self.isOccupied = True
            self.startTime = time_string

    def check_in(self):
        now = datetime.now()
        time_string = now.strftime("%I:%M:%S")
        self.isOccupied = False
        self.endTime = time_string 
        
for index in range(1 , 13):
    pool_table = PoolTable(index)
    Tables.append(pool_table)


  
#Main Menu

print("================================================")
print("|      Welcome to the Pool Table Manager       |")
print("|           by: Eddie Zaboroskie               |")
print("|                                              |")
print("|   Please select from the following options   |")
print("================================================")

while True: 
    print("")
    print("1. Add Players to a Table")
    print("")
    print("2. End a Table Session")
    print("")
    print("3. View All Tables' Status")
    print("================================================")
    print("")


    choice = input("Enter a number from the menu or q to quit: ")
    print("")
    

  
#Choice 1: Check Out a Table

    if choice == "1":
      for pt in Tables:
          print(f"{pt.tableNumber} - Is Occupied: {pt.isOccupied} - Start Time: {pt.startTime} - End Time: {pt.endTime}")
      print("")      
      table_number_check_out = int(input("Enter the table number to add players: "))
      print("")
      if  table_number_check_out >=13 or table_number_check_out <=0:
          print("================================================")
          print("|                   !ERROR!                    |")
          print("================================================")
          print("|   !Enter a Valid Pool Table Number (1-12)!   |")
          print("================================================")
      else:
        pool_table = Tables[table_number_check_out - 1]
        pool_table.check_out()


        
 #Choice 2: Check In a Table and create .txt file with table start/end info 
    
    elif choice == "2":
      for pt in Tables:
          print(f"{pt.tableNumber} - Is Occupied: {pt.isOccupied} - Start Time: {pt.startTime} - End Time: {pt.endTime}")
      print("")   
      table_number_check_in = int(input("Enter the table number to open table: "))
      print("")
      
      if  table_number_check_in >=13 or table_number_check_in <=0:
          print("================================================")
          print("|                   !ERROR!                    |") 
          print("================================================")
          print("|   !Enter a Valid Pool Table Number (1-12)!   |")
          print("================================================")
      
      else:
        pool_table = Tables[table_number_check_in - 1]
        if pool_table.isOccupied == False:
            print("================================================")
            print("|                   !ERROR!                    |") 
            print("================================================")
            print("|       ! This Table Was Not Occupied !        |")
            print("================================================")
        else:
            pool_table.check_in()
        
            now = datetime.now()
            date_string = str(now.strftime("%m - %d - %Y"))
        
            end = datetime.strptime(pool_table.endTime, "%I:%M:%S")
            start = datetime.strptime(pool_table.startTime, "%I:%M:%S")
            total_time= (end - start)
        
            with open(date_string + ".txt" , "a") as file:
                file.write(f"Table #: {table_number_check_in} \n") 
                file.write(f"   Start Time-- {pool_table.startTime} \n")
                file.write(f"   End Time-- {pool_table.endTime} \n")
                file.write(f"   Total Time-- {total_time} \n")
      


#Choice 3: View All Tables 
 
    elif choice == "3":
        for pt in Tables:
            print(f"{pt.tableNumber} - Is Occupied: {pt.isOccupied} - Start Time: {pt.startTime} - End Time: {pt.endTime}")

    elif choice == "q":
        break

#Error message for incorrect menu selection
    else:
        print("================================================")
        print("|                   !ERROR!                    |")
        print("================================================")
        print("|  !Please Select a Valid Menu Option (1 - 3)! |")
        print("================================================")