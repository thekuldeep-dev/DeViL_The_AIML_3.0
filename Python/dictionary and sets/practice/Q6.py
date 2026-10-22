# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique. 

d = {}

for i in range(4):
    name = input(f"Enter friend name{i+1}:")
    fav_subj = input("Enter favorite subject name: ")
    d.update({name:fav_subj})

print(d)    
