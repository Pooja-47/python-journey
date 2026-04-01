# Operations on string:-
# Slicing (print a part of string)
print()
fruit="Mango"
print(len(fruit))  #len() function prints the length of function
print(fruit[0:5])  # includes index 0, excludes index 5
print(fruit[1:4]) # syntax: string[start : end]
print(fruit[:4]) # starting is by default 0
print(fruit[1:]) # ending is by default length-1

# Negative Slicing
print()
print(fruit[:-4]) # python interprets as [0:len(fruit)-4]
print(fruit[-1:4]) # python interprets as [len(fruit)-1:4] print(fruit[-1:4]) 

# print(fruit[-1:4]) returns empty string because start index > end index

name="Harry"
print(name[-4:-2])
