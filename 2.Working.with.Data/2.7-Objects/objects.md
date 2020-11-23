#OBJECTS

More details about Pythons internal object model, memory management, copying and type checking


###ASSIGNMENT
Many operators in Pythin are related to assigning oe storing values:


```python3
a = value         # Assignment to a variable
s[n] = value      # Assignment to a list
s.append(value)   # Appending to a list
d['key'] = value  # Adding to a dictionary
```
Caution: assignment operations NEVER MAKE A COPY of the value being assigned. All assignments are merely reference copies.


Consider the is code:

```python

a = [1,2,3]
b = a
c = [a,b]
```
Above the is only one list object, but there are 4 references to it. (a,b and a,b in c)

This means that modifying a value affects all references:

```python
>>>a.append(999)
>>>a
[1,2,3,999]
>>>b
[1,2,3,999]
>>>c
[[1,2,3,999][1,2,3,999]]
```
A change in the original list shows up everywhere else. This is because no copies were ever made. Everything is pointing to the same thing, a.

###Reassigning Values
Reassigning a value never overwrites the memory used by the previous value.
```python
a = [1,2,3]
b = a
a = [4,5,6]

print(a)	#[4,5,6]
print(b)	#[1,2,3]
```

VARIABLES ARE NAMES. NOT MEMORY LOCATIONS

###Some Dangers:

If you are unaware of this sharing it can cause issues in your code. ie: You modify some data thinking its your own private copy and it accidentally corrupts some data in another part of the program. 

This is one of the reasons why primitive types (int,float,string) are immutabe, read-only.

##Identity and References

Use the ```is```operator to check if two values are exactly the same object

```python

>>> a = [1,2,3]
>>> b = a
>>> a is b
True
```

```is```compares the object identity (as an int). The identity can be obtained using ```id()```

```python
>>>id(a)
3588944
>>>id(b)
3588944
```

It is almost always better to use == for checking objects.

###Shallow Copies

Lists and Dicts have methods for copying.

```python
a = [2,3,[100,101],4]
b = list(a)
a is b
False
```
Its a new list but the list items are shared
```python
a[2].append(102)
b[2]	#[100,101,102]

a[2] is b[2]

True
```

##DEEP COPIES

Sometimes you need to make a copy of an object and all the objects contained within it, You can use the copy module foe this:

```python
a = [2,3,[100,101],4]
import copy
b = copy.deepcopy(a)

a[2].append(102)
b[2]
[100,101]
a[2] is b[2]
False
```
##Names, Values, Types

Variable names do not have a type. Its only a name, but the values do have an underlying type.

```type()``` will tell you what it is. The type name is usually used as a function that creates or converts a value to that type.

##Type Checking

How to tell if an object is a specific type:

```python
if isinstance(a, list):
	print('a  is a list')
```

Checking for one of many possibles types:
```python
if isinstance(a, (list, tuple)):
	print(' a is list, tuple')
```

##EVERYTHING IS AN OBJECT

Numbers, strings, lists, functions, exceptions, instances, etc are all objects. It means that all objects that can be named can be passed around as data, placed in containers etc, without any restrictions. There are no special kinds of objects. 

#EXERCISES

In portfolio.csv we read data organised as columns that looks like this:

```csv
name, shares, prce
'aa', 100, 32.20
...
```
In previous code, we used the csv module to read the file, but still had to perform manual type conversions. ie:

```python
for row in rows:
	name = row[0]
	shares = int(row[1])
	price = float(row[2])
```

This kind of conversion can also be performed in a more clever manner using some basic list operations.

Make a list that contains the names of the conversion functions you would use to convert each column into the appropriate type:

```python
>>>types = [str, int, float]
>>>
```

The reason you can even create this list is that evrything in Python is first-class. So if you want to have a list of functions thats fine. The items in the list you created are functions for converting a value x into a given type (eg, str(x), int(x), float(x))

Now, read a row of data from the above file:

```python
>>> import csv
>>> f = open('Data/portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row 
['AA', '100', '32.20']
>>>