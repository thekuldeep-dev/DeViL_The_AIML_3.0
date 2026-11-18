# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams. 


p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click me"

message = input("Enter your comment: ")
# in is a case sensitive
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("spam message detected!")
else:
    print("not spam")    