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

myList = [1, 2, 3, 4]
myOtherList = [5, 6, 7, 8]

print(myList, myOtherList)
print(myList + myOtherList)

# makeDifferent(myList, myOtherList) # no bueno

def printinfo( arg1, *vartuple ):
   print ("Output is: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return;

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "hi", ["nick", 1, {"name" : "nick"}] )

# prints a log of what was types after prompt
# logs = input("Enter your input: ")
# print ("Received input is : ", logs)

# rotate list left by 1
myList = myList[1:] + myList[:1]

print(myList)

# rotate list left by 1
myList = myList[-1:] + myList[:-1]

print(myList)

# pretty cool
