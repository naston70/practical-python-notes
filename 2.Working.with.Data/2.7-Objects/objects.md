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



