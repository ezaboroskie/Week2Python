ShoppingLists = []

class ShoppingList:
  def __init__(self, store):
    self.store = store
    self.grocery_items = []
                
class GroceryItem:
  def __init__(self, item, price, quantity):
    self.item = item 
    self.price = price
    self.quantity = quantity 

print("Welcome to the Grocery List Manager App!")

while True: 
  print("Enter 1 to create a new shopping list")
  print("Enter 2 to view your lists ")
  print("Enter q to quit")
  choice = input("What would you like to do: ")

  if choice == "1":  
    store_name = input("Enter the store name: ")
    while True:
      
      grocery_item_name = input("Enter a grocery item or enter 'menu' to return to menu: ")
      if grocery_item_name == "menu":
        break
      grocery_price = input("Enter the price of the item: ")
      grocery_quantity = input("Enter the quantity of the item: ")
    
      shopping_list = ShoppingList(store_name)  
      grocery_item = GroceryItem(grocery_item_name, grocery_price, grocery_quantity)
      
    
      shopping_list.grocery_items.append(grocery_item)
      ShoppingLists.append(shopping_list)

  elif choice == "2":
    for shopping_list in ShoppingLists: 
      print("---", shopping_list.store, "---")
      for grocery_item in shopping_list.grocery_items: 
        print("Item:", grocery_item.item)
        print("Price: $", grocery_item.price) 
        print("Quantity:", grocery_item.quantity)

  elif choice == "q": 
    break 
    
  
  

  
    
  




  

 

