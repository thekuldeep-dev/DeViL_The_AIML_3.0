# 2. Write a program to input eight numbers from the user and display all the unique 
# numbers (once). 

unique_numbers = set()

for i in range(8):
    # print(f"Enter no{i+1}: ")
    new_number = int(input(f"Enter no{i+1}: "))
    unique_numbers.add(new_number)

print(unique_numbers)    