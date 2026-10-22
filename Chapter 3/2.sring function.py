name= "Pranjal"

print(len(name)) #length of string
print(name.endswith("al")) #check if string ends with "al"
print(name.startswith("Pr")) #check if string starts with "Pr"
print(name.find("a")) #find the index of first occurrence of "a"    
print(name.upper()) #convert string to upper case
print(name.lower()) #convert string to lower case
print(name.replace("Pranjal", "Python")) #replace "Pranjal" with "Python"
print (name.split("a")) #split string at "a"
print(name.find("a")) #find the index of first occurrence of "a" after index 3


#fstring

name2= "Pranjal"

print(f"My name is {name}") #fstring
