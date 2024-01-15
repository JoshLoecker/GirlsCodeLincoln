def advanced_is_palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    if word == word[::-1]:
        return True
    else:
        return False


def is_palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    
    word_length = len(word) - 1  # Subtract 1 because python is 0 indexed
    for i in range(len(word)):
        if word[i] == word[word_length - i]:
            continue
        else:
            return False
    return True


print(f"Racecar: {is_palindrome('Racecar')}")
print(f"Taco Cat: {is_palindrome('Taco Cat')}")
print(f"My Gym: {is_palindrome('My Gym')}")
print(f"Top Spot: {is_palindrome('Top Spot')}")
print(f"This will fail: {is_palindrome('This will fail')}")
