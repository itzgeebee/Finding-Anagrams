# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) == len(anagram):
        word = word.lower()
        anagram = anagram.lower()
        word = sorted(word)
        anagram = sorted(anagram)

        if word == anagram:
            return True

    return False




