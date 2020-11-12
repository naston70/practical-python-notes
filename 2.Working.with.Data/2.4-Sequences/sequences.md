# SEQUENCES

###Sequence Datatypes

Python has three sequence datatypes:

- String: 'Hello', a sequence of characters
- List: [1,2,3,4]
- Tuple: (5,6,7,8)

All sequences are ordered, indexed by integers and have a length

```python

a = 'hello'
b = [1,4,5]
c = ('good', 100, 490.1)

# They all have indexed order

a[0] # -------> h
b[-1]# -------> 5
c[1] # -------> 100

# All have a length

len(a) #5
len(b) #3
```

Sequences can be replicated: ```s * n```

```python
>>> a = 'Hello'
>>> a * 3
'HelloHelloHello'
>>> b = [1, 2, 3]
>>> b * 2
[1, 2, 3, 1, 2, 3]
>>>
```

Sequences of the same type can be concatenated ```a + b```


## SLICING

Slicing takes a subsequence from a sequence. The syntax is ```s[start:end]```. Where start and end are indexes of the subsequence you want.

```python

a = [0,1,2,3,4,5,6,7,8]

a[2:5] = [2-4]
a[-5]  = [4-8]
a[:3]  = [0-2]
```

Indices (start and end) must be integers
Slices do not include the end value.
If indices are omitted, the default to the beginning or end of the list

## SLICE RE-ASSIGNMENT

On lists, slices can be reassigned and deleted

```python
a = [0,1,2,3,4,5,6,7,8]

del a[2:4]   # [0,1,4,5,6,7,8]
```

## SEQUENCE REDUCTIONS

There are some common functions to reduce a sequence to a single value.

```python
>>> S = [1,2,3,4]
>>> sum(s)
10
>>> min(s)
1
>>> max(s)
4
>>> t = ['hello', 'world']
>>> max(t)
'world'
>>>
```

