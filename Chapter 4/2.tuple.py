a = ()# empty tuple
print(type(a))

b= (1, 2, 3, 4, 5, "Pranjal", 3.14, True, False)# tuple with different data types
print(type(b))
print(b)

t = (10, 20, 30, 20, 40)

print(t.count(20)) # print the count of 20 in the tuple
print(t.index(30)) # print the index of 30 in the tuple
print(len(t))      # print the length of the tuple
print(max(t))      # print the maximum value in the tuple
print(min(t))      # print the minimum value in the tuple
print(sum(t))      # print the sum of all elements in the tuple
print(sorted(t))   # print the sorted tuple
print(t[::-1])     # print the tuple in reverse order
print(20 in t)     # print True if 20 is in the tuple, False otherwise

#opertators in tuple
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2 # concatenation of tuples
print(t3)
t4 = t1 * 3 # repetition of tuples
print(t4)   

print(2 in t1) # membership operator
print(7 not in t2) # not in operator
print(len(t1)) # length of tuple

print(t1>t2) # comparison operator
del t1 # delete the tuple t1
print(t1) # this will raise an error since t1 is deleted

