# String Methods:-
"""Built in methods to alter or modify strings.
Strings are immutable (can't change inplace).
These methods do not make changes in original string they return new strings."""
print()
# 1. upper()
str1="My name is Pooja."
print(str1.upper())

print()
# 2. lower()
str1="HELLOW, POOJA!"  # We can overwrite a variable.
print(str1.lower())

print()
# 3. strip()
str1=" This is strip method  let's try !  "
print(str1.strip())

print()
# 4. rstrip()
str1='!#$ Pooja $##'
print(str1.rstrip("#")) # removes specified characters from the end of the string

print()
# 5. replace()
str1=("Pooja is a student, Pooja works hard.")
print(str1.replace("Pooja","Nirbhay"))

print()
# 6. split()
str1="Pooja is a good girl."
print(str1.split(" "))
print(str1.split("a"))

print()
# 7. capitalize()
str1="capitalize the first letter of string, Rest OTHERS Lower"
print(str1.capitalize())

str1="If the First letter is Capital, No effect (rest to lower)"
print(str1.capitalize())

print()
# 8. center()
str1="Aligns the string to center"
print(len(str1))
print(str1.center(54)) # 14 spaces at start and 14 at end
print(len(str1.center(54)))
print(str1.center(54,"."))

str1="Pooja's World"
print(str1.center(20,"."))

print()
# 9. count()
str1="Counts counts the number of times times a value occured within a string"
print(str1.count("counts")) # Python is case sensitive return 1
print(str1.count("times"))

print()
# 10. endswith()
str1=("checks if string ends with given value and check value in between by giving index")
print(str1.endswith("ex")) # returns either true or false
print(str1.endswith("in",19,20))
print(str1.endswith("if",7,9))
print(str1.endswith("if",4,9))

print()
# 11. startswith()
str1=("Similar to the endswith it tells if string starts with given value.")
print(str1.startswith("Similar"))

print()
# 12. find()
str1="Finds the first occurrence of given value and returns its index. returns -1 if value not present"
print(str1.find("the")) # returns index of first time t
print(str1.find("k"))

print()
# 13. index()
str1=("Same as find but when value not found gives Value_error")
print(str1.index("find")) # returns index of first time 
# print(str1.index("k")) gives error

print()
# 14. isalnum()
str1=("Returns true if string consists of A-Z,a-z,0-9 and false for other than these characters")
print(str1.isalnum())
str1=("ReturnstrueforAtoZand0to9andatoz") # returns False if string contains spaces or special characters
print(str1.isalnum())

print()
# 15. isalpha()
str1=("ReturnsTrueOnlyAlphabetsPresent")
print(str1.isalpha())
str1=("ReturnsFalse09")
print(str1.isalpha())

print()
# 16. islower()
str1=("returns true if all characters of string in lower case")
print(str1.islower())
str1=("REturns FAlse")
print(str1.islower())

print()
# 17. isupper()
str1=("RETURNS TRUE IF ALL CHARACTERS OF STRING IN UPPER CASE")
print(str1.isupper())
str1=("returns FAlSE")
print(str1.isupper())

print()
# 18. isprintable()
str1=("Returns true if all the values within string are printable")
print(str1.isprintable())
str1=("Returns false with characters like\n")
print(str1.isprintable())

print()
# 19. isspace()
str1=("Returns true only if string contains white spaces using tab or spacebar")
str1=("           ")
print(str1.isspace())
str1=("ReturnsFalse")
print(str1.isspace())

print()
# 20. istitle()
str1=("Returns True If First Letter Of Each Word Is Capital.")
print(str1.istitle())
str1=("else returns false")
print(str1.istitle())

print()
# 21. swapcase()
str1=("It converts UPPER CASE to lower case and lower to UPPER CASE")
print(str1.swapcase())

print()
# 22. title()
str1=("It converts the first letter of each word to UPPER CASE rest lower case")
print(str1.title())