class BackpackChifr():
    def __init__(self, message, key_sequence,m,t):
        self.message = message
        self.key_sequence =  key_sequence
        self.translated = ''
        self.m = m
        self.t = t

    def encr(self):
        B = list(map(lambda x: int(x),self.key_sequence.split(',')))
        m = self.m
        t = self.t
        i = 1
        n = len(B)
        A = []
        for elem in B:
            while True:
                ai = elem * t % m
                i += 1
                if i > n:
                    A.append(ai)
                    break
                else:
                    continue

        shifrotext = self.message
        encr_res = []

        for symbol in shifrotext:
            binary_symbol_list = format(ord(symbol), 'b')
            bit_list = [int(x) for x in binary_symbol_list]
            bit_list.insert(0, 0)
            if len(bit_list) != len(A):
                bit_list.insert(0, 0)

            multi_sum = sum(list(map(lambda bit, i: bit * i, bit_list, A)))
            encr_res.append(multi_sum)

        str1 = ', '.join(str(e) for e in encr_res)
        return str1, self.key_sequence

    def decr(self):
        opposite = self.mulinv(self.t,self.m)
        res_arr = []
        decr_list = list(map(lambda x: int(x), self.message.split(',')))

        for item in decr_list:
            cur_oppos = item * opposite%self.m
            binary_str = ''
            sequence = list(map(lambda x: int(x), self.key_sequence.split(',')))

            for i in reversed(sequence):
                if int(i) > cur_oppos:
                    binary_str = str(0) + binary_str
                    continue
                else:
                    differ = cur_oppos - int(i)
                    binary_str = str(1) + binary_str
                    cur_oppos = differ

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



