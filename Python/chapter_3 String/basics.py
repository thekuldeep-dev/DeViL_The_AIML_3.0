name = "Kuldeep"
# string is immutable means we can't able to chanve exisitinig string.

#slicing of string
nameShort = name[0:3]
negative_slicing = name[-7:-4]
slicing = name[4:7]
a = name[1:5]
b = name[-5:-1]
print(nameShort)
print(negative_slicing)
print(slicing)
print(a)
print(b)
print(len(name))


# string reverse
name1 = "DEV"
for i in range(len(name1)-1,-1,-1):
    print(name1[i], end = "")


