# python_1

- \ continuation character
- [] [:] slicing -- 1st number index, second number actual?

eg 
```
list = ['a', 'b', 'c', 'd']
print(list[0:1])
```
result ['a']

but 

```
list = ['a', 'b', 'c', 'd']
print(list[1:1])
```
result []


1. Variables and types

Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable.

- Python allows you to assign a single value to several variables simultaneously. For example −

```
a = b = c = 1
```

- You can also assign multiple objects to multiple variables. For example −

```
a,b,c = 1,2,"john"
```


 - String. 
    - single ('), double (") and triple (''' or """) quotes to denote string
    (triples used for multi-line strings)
    - Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

 - Numbers
    -Python supports four different numerical types −

        - int (signed integers)
        - long (long integers, they can also be represented in octal and hexadecimal)
        - float (floating point real values)
        - complex (complex numbers)
    
    - Number data types store numeric values. They are immutable data types, means that changing the value of a number data type results in a newly allocated object.


 - List
    - The most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them is that all the items belonging to a list can be of different data type.

        - The values stored in a list can be accessed using the slice operator ([ ] and [:]) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.

 - Tuple
    - Read only lists, denoted by parenthesis () instead of brackets []

 - Dictionary
    - Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

        - Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).

        ```
        print dictName.keys()   # Prints all the keys
        print dictName.values() # Prints all the values
        ```