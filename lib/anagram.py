class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        sorted_word = sorted(self.word)
        matches = []
        for word in possible_anagrams:
            if sorted(word) == sorted_word:
                matches.append(word)
        
        return matches
