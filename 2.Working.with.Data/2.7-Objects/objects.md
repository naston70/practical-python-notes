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
```
This row isnt enough to do calculations because the types are wrong, however, the data can be paired up with the types specified in ```types```

```python

>>> types[1]
<type 'int'>
>>> row[1]
'100'
```
Try converting one of the values:

```python
>>> types[1](row[1])	#same as int(row[1])
100
>>>

```
Try converting a different value:

```python
>>> types[2](row[2])
32.2
>>>
```

Try the calculation with converted values:

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000005
>>>
```

Zip the column types with the fields and look at the result.

```python
>>> r = list(zip(types,row))
>>> r
[(<type 'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>, 32.20)]
>>>

```
Notice this has paired a type conversion with a value. ie 'int' is paired with the value '100'.

The zipped list is useful if you want to perform conversions on all of the claues, one after the other.

```python
>>> converted = []
>>> for func, val in zip(type, rows):
		converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.000000005
>>>
```
In the loop, the func variable is one of the type conversion functions (str, int, float) and the val variable is one of the values ('AA', 100, 32.2). The expression func(val) is converting a value.
This code can be compresses into a single list comprehension:

```python

>>> converted = [ func(val) for func, val in zip(types, row) ]
>>> converted
['AA', 100, 32.2]
```
##Exercise 2.25: Making Dictionaries

Remember how the dict() function can easily make a dictionary if you have a sequence of key names and values? We can make a dictionary from the column headers...

```python
>>> headers
['name', 'shares', 'price']
>>> converted
['AA', 100, 32.2]
>>>dict(zip(headers, converted))
```

This can also be done in a single dict-comprehension:

```python
>>> {name: func(val) for name, func, val in zip(headers, types, row)}
```

##EXERCISE 2.26 - BIG PICTURE

Using these techniques you could write statements that easily convert fields from just about any column oriented datafile into a Python dictionary.

```python

f = open('Data/dowstocks.csv')
row = csv.reader(f)
headers = next(rows)
row = next(rows)
>>>headers
['name', 'price', 'date', 'time', 'change', 'open', 'high', 'low', 'volume']
>>>row
['AA', '39.48', '6/11/2007', '9:36am', '-0.18', '39.67', '39.69', '39.45', '181800']
```
This can then be converted using a familiar trick:
```python

>>> types = [str, float, str, str, float, float, float, float, int]

converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
>>>record

{'volume': 181800, 'name': 'AA', 'price': 39.48, 'high': 39.69,
'low': 39.45, 'time': '9:36am', 'date': '6/11/2007', 'open': 39.67,
'change': -0.18}



