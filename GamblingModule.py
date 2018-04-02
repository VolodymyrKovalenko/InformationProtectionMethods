from TritemiusModule import TritemiusChifr

class GamblingChifr(TritemiusChifr):
    def __init__(self, message, key):
        super().__init__(message,key)

    def find_gambling_key(self):
        num_index = 1
        while num_index <= len(self.message):
            self.key = (105*self.key-51) % (len(self.alphabet)-1)
            self.arr_of_keys.append(self.key)
            num_index += 1
