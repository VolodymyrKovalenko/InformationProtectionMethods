class BackpackChifr():
    def __init__(self, message=None, key_sequence=None,m=None,t=None,open_key=None):
        self.message = message
        self.key_sequence =  key_sequence
        self.m = m
        self.t = t
        self.translated = ''
        self.open_key = open_key

    def encr(self):
        res = []
        self.open_key = list(map(lambda x: int(x), self.open_key.split(',')))

        for symbol in self.message:
            binary_symbol_list = format(ord(symbol), 'b')
            bit_list = [int(x) for x in binary_symbol_list]
            bit_list.insert(0, 0)
            if len(bit_list) != len(self.open_key):
                bit_list.insert(0, 0)

            multi_sum = sum(list(map(lambda bit, i: bit * i, bit_list, self.open_key)))
            res.append(multi_sum)

        res = ', '.join(str(e) for e in res)
        return res

    def decr(self):

        opposite = self.mulinv(self.t,self.m)
        res_arr = []
        mes_list = list(map(lambda x: int(x), self.message.split(',')))

        for item in mes_list:
            value = item * opposite%self.m
            binary_str = ''
            private_key = list(map(lambda x: int(x), self.key_sequence.split(',')))

            for i in reversed(private_key):
                if int(i) > value:
                    binary_str = str(0) + binary_str
                    continue
                else:
                    differ = value - int(i)
                    binary_str = str(1) + binary_str
                    value = differ

            binary_result = self.binaryToDecimal(int(binary_str))
            res_arr.append(chr(binary_result))
        str_decrypt = ''.join(res_arr)

        return str_decrypt

    def binaryToDecimal(self,binary):
        decimal, i, n = 0, 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        return decimal

    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    def mulinv(self,b, n):
        g, x, _ = self.egcd(b, n)
        if g == 1:
            return x % n



