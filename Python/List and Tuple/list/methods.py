friends = ["Apple", "Orange", 5, 6.35,78j,False,"Kuldeep"]

print(friends)
print(friends[0])


friends.append("Gautam")

print(friends)

List = [1,98,5,0,4,987,45,18,-19]
List.sort() # its sort no. list in ascending order
print(List)

List.reverse()
print(List)


# insert 

List.insert(3,7895)
print(List)

# pop

pop_value = List.pop(4)
print(pop_value)
print(List)

# remove
remove =List.remove(4)
print(remove)  # its prints none because its cannot return like pop function, its just remove value
print(List)