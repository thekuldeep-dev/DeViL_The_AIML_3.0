name = {
    "kuldeep" : 100,
    "Dev" : 89,
    "Arravya":99,
    "Bholu":23,
    0: "gautam"
}


print(name)
print(name[0])
print(name["Arravya"])

print(name.items())

print(name.keys())  # prints keys
print(name.values())

print(name.get(0)) # same work as name[0] but little difference
# difference is Both methods retrieve the value for an existing key.
# But .get() returns None by default if the key doesn't exist,
#  while square brackets raise a KeyError.


name.update({"kuldeep":78})  # already present values update and new add
print(name)


