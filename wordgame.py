from itertools import permutations

def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        dictionary = {word.strip().lower() for word in file}  # Use a set for O(1) average time complexity lookups
    return dictionary

def get_longest_word(letters, dictionary):
    letters = letters.lower()
    longest_word = ""
    sorted_letters = ''.join(sorted(letters))  # Sort letters to optimize permutation checks

    # Generate permutations sorted by length
    for length in range(1, len(letters) + 1):
        found_longer_word = False
        for perm in permutations(sorted_letters, length):
            perm_word = ''.join(perm)
            if perm_word in dictionary:
                if len(perm_word) > len(longest_word):
                    longest_word = perm_word
                    found_longer_word = True
            elif found_longer_word:
                # If we found a longer valid word, we can stop further permutations of this length
                break
        
        # Early exit if no longer words can be found
        if not found_longer_word:
            break

    return longest_word


dictionary_file = "words.txt"  # Replace with your dictionary file path

try:
    dictionary = load_dictionary(dictionary_file)
except FileNotFoundError:
    print(f"Error: Dictionary file '{dictionary_file}' not found.")
    exit(1)
except Exception as e:
    print(f"Error loading dictionary file: {e}")
    exit(1)

letters = input("Enter 9 letters: ").strip()

if len(letters) != 9:
    print("Please enter exactly 9 letters.")
else:
    longest_word = get_longest_word(letters, dictionary)
    if longest_word:
        print(f"The longest word is: {longest_word}")
    else:
        print("No valid words found.")