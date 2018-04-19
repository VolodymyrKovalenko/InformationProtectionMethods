import math
import random
import re

class BookingChifr():
    def __init__(self, message, key):
        self.message = message
        self.key = key
        self.result_translated = ''
        self.arr_of_split_key = []

    def split_booking_key(self):
        for line in self.key.splitlines():
            self.arr_of_split_key.append(list(line))
        if len(self.arr_of_split_key) == 0:
            return 'Sorry, enter key'

    def encr_booking(self):

        for symbol in self.message:
            find_symbol = False
            res_str = ''
            startRow = random.randint(0,len(self.arr_of_split_key)-1)

            for i in range(startRow,len(self.key.splitlines())):
                try:
                    encr_symbol_index = self.arr_of_split_key[i].index(symbol)
                    res_str = '{}/{},'.format(str(i),str(encr_symbol_index))
                    find_symbol = True
                    break
                except ValueError:
                    continue

            if find_symbol == False:
                for i in range(0,startRow):
                    try:
                        encr_symbol_index = self.arr_of_split_key[i].index(symbol)
                        res_str = '{}/{},'.format(str(i), str(encr_symbol_index))
                        find_symbol = True
                        break
                    except ValueError:
                        continue

            if find_symbol == False:
                return 'Sorry, {} symbol does not exist in verse key'.format(symbol)
            else:
                self.result_translated += res_str
        return self.result_translated

    def decr_booking(self):
        mess = self.message.split(',')
        for part in mess:
            if part == '':
                break
            print(part)
            if re.match(r'\d+\/\d+',part) == None:
                return 'Sorry, enter correct message'

            parts = part.split('/')
            row_symb = int(parts[0])
            col_symb = int(parts[1])
            try:
                decr_symbol = self.arr_of_split_key[row_symb][col_symb]
                self.result_translated += decr_symbol
            except IndexError:
                return 'Sorry, {} symbol does not exist in verse key'.format(part)
        return self.result_translated

