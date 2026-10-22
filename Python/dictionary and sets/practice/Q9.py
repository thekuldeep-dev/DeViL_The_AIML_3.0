# 9. Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}

s.remove(8)
s.add(19)
print(s)

# its give error due to 2 reasons

# 1. we can't able to include list in set
# 2. and in set indexing not working(not hashable)