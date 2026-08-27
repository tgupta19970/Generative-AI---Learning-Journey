# Task 2 - Create a Another Module (string_utils.py)

# Capitalized word function
def capitalize_words(word):
    return word.title()


# Reverse String function
def reverse_string(text):
    reverseStr = ""
    for i in range(len(text)):
        reverseStr = text[i] + reverseStr

    return reverseStr


# Word count function
def word_count(text):
    # Split the text to words
    words = text.split()

    # Count the words
    count = len(words)

    return count