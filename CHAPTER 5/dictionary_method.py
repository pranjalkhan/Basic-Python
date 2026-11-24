a = { 
"key": "value", 
"pranjal": "code", 
"marks": "100", 
"list": [1, 2, 9] 
} 
print(a["key"])  # Output: "value" 
print(a["list"])  # Output: [1, 2, 9] 

a.update({"key": "new_value"})  # Update the value of "key"
print(a)
a.update({"marks": "95"})  # Update the value of "marks"
print(a)

d = {"a": 10, "b": 20}
d.clear()
print(d)

d = {"a": 10, "b": 20}
x = d.copy()
print(x)

#-------------------------------------------------------------------------------------------------


# 1. clear()
d = {"a": 10, "b": 20}
d.clear()
print("clear():", d) # clear the dictionary

# 2. copy()
a = {"a": 10, "b": 20}
x = a.copy()
print("copy():", x) # copy the dictionary

# 3. fromkeys()
keys = ("a", "b", "c")
x = dict.fromkeys(keys, 0)
print("fromkeys():", x) # create a new dictionary with keys from the given sequence and values set to 0

# 4. get()
b = {"name": "Rahim", "age": 20}
print("get():", b.get("name")) # get the value of the key "name"

# 5. items()
c = {"a": 10, "b": 20}
print("items():", c.items()) # get a view object that displays a list of a dictionary's key-value tuple pairs

# 6. keys()
print("keys():", c.keys()) # get a view object that displays a list of a dictionary's keys

# 7. values()
print("values():", c.values()) # get a view object that displays a list of a dictionary's values

# 8. pop()
e = {"a": 10, "b": 20}
e.pop("a")
print("pop():", e) # remove the key-value pair with the key "a"

# 9. popitem()
f = {"a": 10, "b": 20} 
f.popitem()
print("popitem():", f) # remove and return an arbitrary key-value pair

# 10. setdefault()
g = {"a": 10, "b": 20}
g.setdefault("c", 30)
print("setdefault():", g) # add a new key-value pair if the key is not already in the dictionary

# 11. update()
h = {"a": 10, "b": 20}
h.update({"c": 30})
print("update():", h) # add or update key-value pairs in the dictionary

