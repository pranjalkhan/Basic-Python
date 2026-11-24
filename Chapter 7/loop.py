for i in range(1, 6):
    print(i)

# num = 5

# for i in range(1, 11):
#     print(num, "x", i, "=", num*i)

# i = 1

while i <= 5:
    print(i)
    i += 1


l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0

while(i < len(l)):
    print(l[i])
    i += 1


#for loop with else 
for i in range(1, 6):
    print(i)
else:
    print("Loop finished.")

#for loop with break
for i in range(1, 6):
    if i == 3:
        break #exit the loop when i is 3
    print(i)

#for loop with continue
for i in range(1, 6):
    if i == 3:
        continue #skip the iteration when i is 3
    print(i)


#for loop with pass
for i in range(1, 6):
    if i == 3:
        pass #do nothing when i is 3
    else:   #when i is not 3, print the value of i
        print(i)    

