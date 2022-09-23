#Classes are a blue print

class Car:
    def __init__(self, make, model, color): #initializer or constructor
        self.make = make
        self.model= model
        self.color= color
        self.vin= "" #undefined right now

car = Car("Honda", "Accord", "White") #creating a Car object and putting it in a variable called car
print(car.make)
print(car.model)


car2 = Car("Tesla", "Model X", "Red")

print(car2.make)
print(car2.model)
print(car2.color)

class Table:
  def __init__(self, height, shape, material):
    self.height= height
    self.shape= shape
    self.material= material 

table1 = Table("Tall", "Round", "Wood")
print(table1.height)
print(table1.shape)
print(table1.material)

table2 = Table("Short", "Square", "Plastic")
print(table2.height)
print(table2.shape)
print(table2.material)



class User:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name= last_name
    self.addresses= []

class Address: 
  def __init__(self, street, city, state, zip_code,):
    self.street = street
    self.city = city
    self.state = state
    self.zip_code = zip_code
    

user=User("Eddie", "Zaboroskie")
address = Address("555 Madeup Rd", "Atlanta", "GA", "30339")
address2 = Address("999 Makebelieve Rd", "New York", "NY", "34838")

user.addresses.append(address)
user.addresses.append(address2)

for address in user.addresses:
  print(address.street)


class BankAccount: 
  def __init__(self, account_number, balance): 
    self.account_number = account_number 
    self.balance = balance 

  def deposit(self, amount):
    self.balance += amount  

# ASKING FOR INPUT 
account_number = input("Enter account number: ")
balance = float(input("Enter balance: ")) 

checking_account = BankAccount(account_number, balance)
deposit_amount = float(input("Enter amount to deposit: ")) 
checking_account.deposit(deposit_amount)

print(checking_account.balance)    