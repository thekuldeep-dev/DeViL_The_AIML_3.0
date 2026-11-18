a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = int(input("Enter d:"))

if(a>b & a>c & a>d):
    print("a is greater: ",+a)
elif(b>a & b>c & b>d):
    print("b is greater: ",b)
elif(c>b & c>a & c>d):
    print("c is greater: ",c)
else:
    print("d is greater: ",d)

print("End of program!")    