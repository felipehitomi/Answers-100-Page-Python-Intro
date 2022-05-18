def anagram(word1, word2):
    return print(sorted(word1.lower()) == sorted(word2.lower()))

anagram('god', 'Dog')
anagram('beat', 'table')
anagram('Beat', 'abet')
anagram('Beatt', 'abtet')
