
stores = []

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = []

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


while True:
  print("1. Add a Shopping List: ")
  print("")
  print("2. Add Item(s) to a Shopping List: ")
  print("")
  print("3. View All Shopping Lists: ")
  print("")
  print("4. Delete a Shopping List: ")
  print("")
  print("5. Delete an item from a list: ")
  print("")
  print("q: Quit")
  print("")

  choice = input("Make a selection by entering the number or q to quit: ")
  print("")

  try:

    if choice == "1":
      store_name = input("Enter a store name: ")
      store_address = input("Enter the store address: ")
      print("")
      store = Store(store_name, store_address)
      stores.append(store)

    elif choice == "2":
    
      for index in range(0, len(stores)):
        print(f"{index +1}. {stores[index].name} - {stores[index].address}")

      print("")
      store_number = int(input("Enter store number to add item to list: "))
      store = stores[store_number -1]
    
      while True:
        item_name = input("Enter item name or 'menu' to return to Main Menu: ")
        if item_name == "menu":
          break
        item_price = float(input("Enter item price: ")) 

        item = Item(item_name, item_price)
        store.items.append(item)
    
    elif choice == "3":
      for index in range (0, len(stores)):
        store = stores[index]
        print(f"{index + 1}. {store.name} - {store.address}")
        for item in store.items:
          print("-" , item.name )
          print("$", item.price)

    elif choice == "4":
      for index in range(0, len(stores)):
        print(f"{index +1}. {stores[index].name} - {stores[index].address}")
      store_id = int(input("Enter the store number that you would like to delete: "))
      del stores[store_id - 1]

    elif choice == "5":
      for index in range(0, len(stores)):
        print(f"{index +1}. {stores[index].name} - {stores[index].address}")
      store_id = int(input("Enter the store number that you would like to delete an item from: "))
      shopping_list = stores[store_id - 1]
      for index in range(0,len(shopping_list.items)):
        item = shopping_list.items[index]
        print(f"{index + 1}. {item.name}")
      item_id = int(input("Enter the item number that you would like to delete: "))
      del shopping_list.items[item_id - 1]
      
    
    
  
    elif choice == "q":
      break
  
  except IndexError:
    print("Input Not Accepted")
  except ValueError:
    print("Input Not Accepted")
  except:
    print("Unknown Error")