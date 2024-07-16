import itertools
import tkinter as tk

wordlist = []

with open('words.txt', 'r') as file:
    valid_words = set(file.read().split())

   
letters = (input("Enter the letters: "))
letters= list(letters)
print(letters)

print("Letters:", letters)

allorders = list(itertools.permutations(letters))

for order in allorders:
    word = ''.join(order)
    if word in valid_words:
        wordlist.append(word)


wordlistwithoutdupes = list(set(wordlist))

for words in wordlistwithoutdupes:
    print(words)