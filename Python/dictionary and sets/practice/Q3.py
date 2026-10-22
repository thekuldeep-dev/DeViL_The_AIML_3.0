# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?

s = set()
s.add(18)
s.add('18')


print(s)   # yes, both as values stored because both are different one is int or other is string