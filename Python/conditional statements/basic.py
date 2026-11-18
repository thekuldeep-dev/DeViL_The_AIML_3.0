a = int(input("Enter your age: "))
# input giveoutput in string that reason we typecast in int

# If elif else ladder
if(a>=18):
    print("Able to vote!")
elif(a<0):
    print("Invalid negative entry!, you're mad!!")
elif(a==0):
    print("Invalid , zero age")    
else:
    print("You are not able to vote.")        

print("End of program")