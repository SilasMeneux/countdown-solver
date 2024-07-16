import itertools
import tkinter as tk
letters =[]

with open('words.txt', 'r') as file:
    valid_words = set(file.read().split())

for i in range (9):    
    letters.append(input("Enter the letter: "))
print("Letters:", letters)

allorders = list(itertools.permutations(letters))

for order in allorders:
    word = ''.join(order)
    if word in valid_words:
        break





root = tk.Tk()
root.title("Text Display Example")
root.geometry("400x300") 


text_label = tk.Label(root, text="The word is: "+ word)
text_label.pack(pady=20, padx=50)  
root.lift()



root.mainloop()