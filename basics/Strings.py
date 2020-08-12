# simple string
x = 'Hello World'
print(x)

# multiline string
x = '''Hi I 
am a multiline
string'''
print(x)

# strings as arrays just like C++
print(x[6])

# getting a substring or we can say that slicing a string
print(x[2: 8])

# if we want to start from behind we use negative indexing
print(x[-4: -1])

# length of string using len()
print(len(x))

# strip() will remove extra spacing infront and back of string
x = ' Hello World '
print(x.strip())

# contains() in case of string in python
print('wor' in x)

# !contains() in case of string in python
print('wor' not in x)

# multiple outputs in a single string using format() and {}
x = 'I want {} pieces of item {} for {} dollars'
print(x.format(5, 'Chocolates', 10))

x = 'Hello World'
print(x.isspace())
