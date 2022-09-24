def MainMenu():

  print("====================================")
  print("| Welcome to the Word Analizer App |")
  print("|      by: Eddie Zaboroskie        |")
  print("====================================")
  print("1: Anagram Finder")
  print("")
  print("2: Palindrome Finder")
  print("")
  print("Please select from the following options") 
  print("or enter 'menu' at anytime to return ") 
  choice = input("to main menu: ")
  print("")

  
  if choice == "1":
    anagramFunc()
  elif choice == "2":
    palindromeFunc()
  elif choice == "menu":
    MainMenu()

def anagramFunc():
  
  from collections import Counter 
  print("===============================")
  print("|      Finding Anagrams       |")
  print("===============================")
  while True:

    def is_anagram(string1, string2):
      return Counter(string1.casefold()) == Counter(string2.casefold())
    
    word1 = input("Enter the first word or 'menu': ")
    print("")
    if word1 == "menu":
      MainMenu()
    word2 = input("Enter the second word or 'menu': ")
    print("")
    if word2 == "menu":
      MainMenu()

    elif is_anagram(word1 , word2):
      print("     *********************************")
      print("     |    These words are anagrams   |")
      print("     *********************************")
      print("")
      print("")
    else:
      print("     *********************************")
      print("     |  These words are not anagrams |")
      print("     *********************************")
      print("")
      print("")

def palindromeFunc():

  print("===============================")
  print("|     Palindrome Checker      |")
  print("===============================")
  while True:

    def is_palindrome(word):
      if word.casefold() == word[::-1].casefold():
        return True

    word1 = input("Enter a word or 'menu': ")
    print("")
    if word1 == "menu":
      MainMenu()
    elif is_palindrome(word1):
      print("     *****************************")
      print("     | This word is a palindrome |")
      print("     *****************************")
      print("")
      print("")
    else:
      print("     *********************************")
      print("     | This word is not a palindrome |")
      print("     *********************************")
      print("")
      print("")

MainMenu()
