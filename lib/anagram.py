# your code goes here!
# anagram.py

class Anagram:

    def __init__(self, word):
        self.word = word
        self.matches = []

    def match(self, words):
        for word in words:
            if self.word != word and sorted(self.word) == sorted(word):
                self.matches.append(word)
        return self.matches