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
