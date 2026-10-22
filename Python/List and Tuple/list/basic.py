# Python lists are containers to store a set of values of any data type.
friends = ["Apple", "Orange", 5, 6.35,78j,False,"Kuldeep"]

print(friends)
print(friends[0])

# string[3] = "h" not possible due to string is immutable

friends[1] = "Mango"  # but in list this is possible because list are mutable
print(friends)
