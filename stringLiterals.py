# String Literals
print("Hello World!")

# Assign String to a Variaable
a = "Hello"
print(a)

# Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# or with three quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings are Arrays
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])


# slicing

b = "Hello, World!"
print(b[2:5])


# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])

# String Length
a = "Hello, World!"
print(len(a))

# String Methods
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# Check String
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check if the phrase "ain" is NOT present in the following text
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# String Concatenation
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# For Escape characters, String Methods visit link below.
# https://www.w3schools.com/python/python_strings.asp
