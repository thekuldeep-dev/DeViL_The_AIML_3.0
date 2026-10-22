# 4. What will be the length of following set s:
# imp question

s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations?

print(len(s)) #its output is 2
# because python show true of 2 ==2.0


# 10 and 10.0 are equal, and True and 1 are equal. The string "1" is different. So there are 3 unique elements.