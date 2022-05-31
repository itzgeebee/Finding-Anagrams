# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word) == len(anagram):
        word = word.lower()
        anagram = anagram.lower()
        count = 0
        for i in anagram:
            if i in word:
                count += 1
        if count == len(word):
            return True

    return False



