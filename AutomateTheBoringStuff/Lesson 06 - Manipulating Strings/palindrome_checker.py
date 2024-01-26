# The following is pseudocode and is not meant to be run

def advanced_is_palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


Create a function called 'is_palindrome' that accepts an argument called 'word'
    Remove all spaces from the word
    Convert the word to lowercase
    Create a variable called 'word_length' and set it to the length of the word minus 1
    Loop through the word
        If the letter at the current index is equal to the letter at the index of 'word_length' minus the current index
            Continue
        Else
            Return False
    Return True


# Use the following code to test if your function works
print("Racecar: " + str(is_palindrome("Racecar")))
print("Taco Cat: " + str(is_palindrome("Taco Cat")))
print("Hello World!: " + str(is_palindrome("Hello World!")))
print("This will fail: " + str(is_palindrome("This will fail")))
