# Detect double space in string

name = "My bame  is Kuldeep Gautam  But you are an IPS officer"
print(name.find("  "))  # its only tells the index value where its find first but if not able to find return -1


# Q4 replace double space with single space

print(name.replace("  "," "))  # its replace all possible
print(name) # its print all original because strings are immutable