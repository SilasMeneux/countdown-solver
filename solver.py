import itertools
import tkinter as tk
letters =[]
wordlist = []

with open('words.txt', 'r') as file:
    valid_words = set(file.read().split())

for i in range (9):    
    letters.append(input("Enter the letter: "))
print("Letters:", letters)

allorders = list(itertools.permutations(letters))

for order in allorders:
    word = ''.join(order)
    if word in valid_words:
        wordlist.append(word)




for words in wordlist:
    print(words)