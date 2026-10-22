# 1. Write a program to create a dictionary of Hindi words with values as their English 
# translation. Provide user with an option to look it up!
words = {
    "madad" : "Help",
    "kursi" : "chair",
    "kutta" : "Dog",
    "hathi" : "Elephant"
}

word = input("Enter word that meaning you want: ")
print(f"translation of that word :{words.get(word)}")