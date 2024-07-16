from itertools import permutations

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = [word.strip().lower() for word in file]
    return dictionary

def get_longest_word(letters, dictionary):
    letters = letters.lower()
    longest_word = ""

    # Generate all permutations of the letters
    for length in range(1, len(letters) + 1):
        for perm in permutations(letters, length):
            perm_word = ''.join(perm)
            if perm_word in dictionary and len(perm_word) > len(longest_word):
                longest_word = perm_word

    return longest_word

if __name__ == "__main__":
    dictionary_file = "words.txt"  # Replace with your dictionary file path
    dictionary = load_dictionary(dictionary_file)
    
    letters = input("Enter 9 letters: ").strip()
    
    if len(letters) != 9:
        print("Please enter exactly 9 letters.")
    else:
        longest_word = get_longest_word(letters, dictionary)
        if longest_word:
            print(f"The longest word is: {longest_word}")
        else:
            print("No valid words found.")