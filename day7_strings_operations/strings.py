# Strings:-
"""Enything we enclose btw single orr double quotes is considered as string.
String is sequence orr like an array of characters.
"""
print()
print("This is a string")
name="Pooja"
print('My name is:'+name)

# Multiline strings:-
print()
print("""This is a multiline string.
Hello, this is Pooja.
BTech 4th sem CSE student.
CS-B (24EARCS111) """)

# Sometimes user might need to put "" or '' marks btw the string this can be done as:-
print()
# 1. Escape sequence characters /"" or /'
print("This string consists double quotes using \"Escape sequence charactrs\"")
print('This string consists single quotes using \'Escape sequence charactrs\'')
# 2. use '' for string
print('This string consists "double quotes"')
print("This string consists 'single quotes'")

print()
# Accessing the characters of a string:-
Access="We can access the characters of string using index"
print(Access[0])  # indexing starts from 0 ends at (length of string)-1
print(Access[1])
# Using for loop:
print("using for loop:")
for character in Access:
    print(character)