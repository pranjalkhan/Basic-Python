my_list = ["apple", "banana", "cherry", 5 ,35, 3.5, True, False]

print(my_list[0]) #slicing of list
print(my_list[1]) #slicing of list
print(my_list[2]) #slicing of list

my_list[0] = "orange" #changing the value of list
print(my_list[0]) #slicing of list
my_list.append("grapes") #adding the value to list
print(my_list) #printing the list

num_list = [5, 44, 43, 24, 35]
print(num_list) #printing the list

sorted_list = sorted(num_list) #sorting the list
print(sorted_list)

reverse_list = sorted(num_list, reverse=True) #sorting the list in reverse order
print(reverse_list)

num_list.insert(2, 100) #inserting the value at index 2
print(num_list) #printing the list


num_list.pop(2) #removing the value at index 2
print(num_list) #printing the list



num_list.remove(44) #removing the value 44 from the list
print(num_list) #printing the list

