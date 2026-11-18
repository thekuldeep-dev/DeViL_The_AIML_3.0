# 5. Write a program which finds out whether a given name is present in a list or not.

students = ["Kuldeep", "Samiara", "Aadhya","Deep"]
# in keyword is case sensitive so rememebr this
name = input("Enter your name: ")


if(name in students):
    print("your name is already in list of students")
else:
    print("YOur name is not list, so sorry for that!")   