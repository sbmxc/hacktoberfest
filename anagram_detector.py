def are_anagrams(word1, word2):
    clean_word1 = word1.replace(' ', '').lower()
    clean_word2 = word2.replace(' ', '').lower()

    if len(clean_word1) != len(clean_word2):
        return False

    sorted_word1 = sorted(clean_word1)
    sorted_word2 = sorted(clean_word2)

    return sorted_word1 == sorted_word2

word1 = "listen"
word2 = "silent"

if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:

    print(f"{word1} and {word2} are not anagrams.")
