msg = "Hello World"
print (msg)

string = "asdf"

print(string[::-1])

# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']

# print(list)         # Prints complete list
# print(list[0])       # Prints first element of the list
# print(list[1:3])     # Prints elements starting from 2nd till 3rd 
# print(list[2:])      # Prints elements starting from 3rd element
# print(tinylist * 2)  # Prints list two times
# print(list + tinylist) # Prints concatenated lists

list = ['a', 'b', 'c', 'd']
print(list[1:3])

var = 100
if ( var == 100 ) : print ("Value of expression is 100")
print("Good bye!")

import calendar

cal = calendar.month(2020, 12)
print ("Here is the calendar:")
# print (cal)

def printme(str):
    print(str)
    return

printme(cal)

def makeDifferent(thing):
    thing = "yo"
    print("yo", thing)    
    return

same = 2

print(same)
makeDifferent(same)