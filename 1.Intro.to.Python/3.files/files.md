### FILE MANAGEMENT

Alot of programs need to read input from somewhere.

# File Input and Output 

Open a file:

```python
f = open('foo.txt', 'rt') # open for reading
g = open('foo.txt', 'wt') # open for writing
```

Read all the data

```python

data = f.read()
# read only up to 'maxbytes'

data = f.read([maxbytes])
```

Write some text

```python
g.write('some text')
```

Close the files when finished

```python
g.close()
f.close()
```

Files should be properly closed, preferred approach is to use the ```with```statement to open

```python

with open (filename, 'rt') as my_file:
	# use the file my_file
	# no need to close
```

This automatically closes the file when control leave the indented block


### COMMON IDIOMS FOR READING FILE DATA

Read an entire file all at once as a string.
```python
with open('some.txt', 'rt') as my_file:
	data = file.read()
```

Read a file line by line by iterating.

```python

with open(filename, 'rt') as file:
	for line in file:
		# do something 
```
### Common idioms for Writing to a File.

Write string data.
```python
with open('outfile', 'wt') as out:
	out.write('Hello World\n')

```

Redirect the print function.

```python

with open('outfile', 'wt') as out:
	print('Hello World', file=out)

```

### EXERCISES.

Exercises depend on Data/portfolio.csv (moved Work to local folder)

# completed pcost.py

