# its same as list but its immutable like string

a = (1,2,3,4,5,6)
print(type(a))

# empty tuple
a = ()

# one element tuple
b = (1,)


t1 = (12,45,-4,-19,"Kuldeep","Arravya",False)
print(type(t1))



# tuple supports unpacking but need same no. of variable as no. of data
tupl = (1,5,"Hello")
a,b,c = tupl
print(a,b,c)
