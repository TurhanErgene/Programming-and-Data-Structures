class WordFrequency:
    def __init__(self, word):
        self.word = word
        self.frequency = 1

    def __str__(self):
        return f'{self.word}: {self.frequency}'

    def __hash__(self):
        return hash(self.word)

    def __eq__(self, other):
        if other is None:  # Safeguard against NoneType comparison
            return False
        return isinstance(other, WordFrequency) and self.word == other.word
