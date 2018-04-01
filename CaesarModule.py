class CaesarChifr():
    def __init__(self, message, key):
        self.message = message
        self.key = key
        self.translated = ''
        self.alphabet = []
    def CreateAlphabet(self):
        self.alphabet = list(map(chr, range(0, 2001)))

    def encr(self):
        for symbol in self.message:
            num = (ord(symbol)+self.key) % len(self.alphabet)
            self.translated += chr(num)
        return self.translated

    def decr(self):
        for symbol in self.message:
            num = (ord(symbol)+len(self.alphabet) - (self.key % len(self.alphabet))) % len(self.alphabet)
            self.translated += chr(num)
        return self.translated
