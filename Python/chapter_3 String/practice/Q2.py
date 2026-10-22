# name = input("Enter your name: ")
# Date = int(input("Enter date: "))
# # we use fstring
# letter = f'''
#     Dear {name},
#     You are Selected!
#     {Date}
# '''

# print(letter)


letter = ''' Dear <|Name|>,
You are selected!
<|Date|>'''

print(letter.replace("<|Name|>","Kuldeep").replace("<|Date|>","19"))  # so we able to chaining .replace function