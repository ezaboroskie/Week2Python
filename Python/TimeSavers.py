#==============================================#
#==============================================#
########### Swapping Two Values ################

a, b = 5 , 10

##Method 1
a, b = b , a 
##MEthod 2
def swap(a,b):
    return b,a
swap(a,b)
        #Expected Output: 
            # a, b = 10, 5

#==============================================#
#==============================================#
####### Combining a List of Strings ############

List = ["Hello", "world", "Ok" , "Bye!"]
combined_string = "".join(list)

print(combined_string)
        #Expected Output: 
            # "Hello world Ok Bye!"

#==============================================#
#==============================================#
############ Reversing a String ################

string = "Hello World"

print("Reversed string is: " , string[::-1])
        #Expected Output:
            # Reversed string is: dlroW olleH

#==============================================#
#==============================================#
###### Finding Element of Most Occurance #######

def most_frequent(list):
    return max(set(list), key=list.count)

mylist = [1,1,2,3,4,5,6,6,2,2]
print("Most Frequent Item is: " , most_frequent(mylist))
        #Expected Output:
            # Most Frequent Item is: 2

#==============================================#
#==============================================#
################# Anagrams #####################

from collections import Counter 

def is_anagram(string1, string2):
    return Counter(string1) == Counter(string2)

print(is_anagram('race', 'care'))
print(is_anagram('abcd', 'dbca'))
        #Expected Output:
            # True 
            # True

#==============================================#
#==============================================#        
