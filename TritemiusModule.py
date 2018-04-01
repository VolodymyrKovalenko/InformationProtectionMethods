from CaesarModule import CaesarChifr

class TritemiusChifr(CaesarChifr):
    def __init__(self, message, key):
        super().__init__(message,key)
        self.arr_of_keys = []


    def find_key(self):
        num_index = 1
        if len(self.key) == 1:
            i = iter(self.key[0])
            while num_index <= len(self.message):
                try:
                    k = ord(next(i))
                except StopIteration:
                    i = iter(self.key[0])
                    k = ord(next(i))
                self.arr_of_keys.append(k)
                num_index += 1
        else:
            while num_index <= len(self.message):
                if len(self.key) == 3:
                    k = int(self.key[0]) * num_index ** 2 + int(self.key[1]) * num_index + int(self.key[2])
                elif len(self.key) == 2:
                    k = int(self.key[0]) * num_index + int(self.key[1])
                else:
                    k = 0
                self.arr_of_keys.append(k)
                num_index += 1


    def encr(self):
        i = iter(self.arr_of_keys)
        for symbol in self.message:
            try:
                k = next(i)
            except StopIteration:
                i = iter(self.arr_of_keys)
                k = next(i)

            num = (ord(symbol)+k) % len(self.alphabet)
            self.translated += chr(num)

        return self.translated

    def decr(self):
        i = iter(self.arr_of_keys)
        for symbol in self.message:
            try:
                k = next(i)
            except StopIteration:
                i = iter(self.arr_of_keys)
                k = next(i)
            num = (ord(symbol)+len(self.alphabet) - (k % len(self.alphabet))) % len(self.alphabet)
            self.translated += chr(num)

        return self.translated