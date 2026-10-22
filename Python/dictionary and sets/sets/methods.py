s = {1,5,8,"Kuldeep","Arravya","Gautam",78.23}

print(s,type(s))

# imp is add()
s.add("Hello World")
print(s)
print(len(s))



# union prints values that in both sets but dont repeat

s1 = {1,45,78,2}
s2 = {1,456,78.2,2}

print(s1.union(s2))
# intersrction prints common value from different sets
print(s1.intersection(s2))

# also learn s1-s2 or s2-s1