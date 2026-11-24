
# 1. add()
s = {10, 20, 30}
s.add(40)
print("add():", s) # add an element to the set

# 2. clear()
s = {10, 20, 30}
s.clear()
print("clear():", s) # clear the set

# 3. copy()
s = {10, 20, 30}
x = s.copy()
print("copy():", x) # copy the set

# 4. remove()
s = {10, 20, 30}
s.remove(20)
print("remove():", s) # remove an element from the set

# 5. discard()
s = {10, 20, 30}
s.discard(40)
print("discard():", s) # remove an element from the set if it exists

# 6. pop()
s = {10, 20, 30}
x = s.pop()
print("pop():", x, s) # remove and return an arbitrary element from the set

# 7. update()
s = {10, 20}
s.update([30, 40])
print("update():", s) # add elements to the set

# 8. union()
a = {1, 2, 3}
b = {3, 4, 5}
print("union():", a.union(b)) # return a set containing all elements from both sets

# 9. intersection()
print("intersection():", a.intersection(b)) # return a set containing elements that are in both sets

# 10. difference()
print("difference():", a.difference(b)) # return a set containing elements that are in the first set but not in the second set

# 11. symmetric_difference()
print("symmetric_difference():", a.symmetric_difference(b)) # return a set containing elements that are in either set but not in both sets

# 12. intersection_update()
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print("intersection_update():", a) # update the set with the intersection of itself and another set

# 13. difference_update()
a = {1, 2, 3}
b = {2, 3, 4}
a.difference_update(b)
print("difference_update():", a) # update the set with the difference of itself and another set

# 14. symmetric_difference_update()
a = {1, 2, 3}
b = {2, 3, 4}
a.symmetric_difference_update(b)
print("symmetric_difference_update():", a) # update the set with the symmetric difference of itself and another set

# 15. issubset()
a = {1, 2}
b = {1, 2, 3, 4}
print("issubset():", a.issubset(b)) # check if the set is a subset of another set

# 16. issuperset()
print("issuperset():", b.issuperset(a)) # check if the set is a superset of another set

# 17. isdisjoint()
a = {1, 2, 3}
b = {4, 5, 6}
print("isdisjoint():", a.isdisjoint(b)) # check if the sets have no elements in common
