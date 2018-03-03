from flask import Flask,render_template,request,redirect, url_for, jsonify, json
import string
import re

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def firstPost():

    if request.method == 'POST':
        if 'form1' in request.form:
            encr_text = request.form['TextEncr']
            input_key = int(request.form['InpKey1'])
            obj = EncryptMessage(encr_text,input_key)
            obj.CreateAlphabet()
            res_message = obj.encr()
            return render_template('MainPage.html',my_data1=res_message)
        elif 'form2'in request.form:
            decr_text = request.form['TextDecr']
            input_key = int(request.form['InpKey2'])
            obj = EncryptMessage(decr_text, input_key)
            obj.CreateAlphabet()
            res_message = obj.decr()
            return render_template('MainPage.html', my_data2=res_message)

    return render_template('MainPage.html')

@app.route('/tritemius', methods=['GET', 'POST'])
def TritemiusPost():
    eror = 'Enter all the fields'
    if request.method == 'POST':
        input_array = []
        if 'form1' in request.form:
            encr_text = request.form['TextEncr']
            if len(request.form['InpKey1']) != 0:
                input_array.append(request.form['InpKey1'])

            elif len(request.form['InpKey21']) != 0:
                if len(request.form['InpKey22']) != 0:
                    input_array.extend((int(request.form['InpKey21']),int(request.form['InpKey22'])))
                else:
                    return render_template('TritemiusPage.html',er_info=eror)

            else:
                if len(request.form['InpKey31']) != 0 and len(request.form['InpKey32']) != 0 and len(request.form['InpKey33']) != 0:
                    input_array.extend((int(request.form['InpKey31']),int(request.form['InpKey32']),int(request.form['InpKey33'])))
                else:
                    return render_template('TritemiusPage.html',er_info=eror)

            obj = TritemiusChifr(encr_text,input_array)
            obj.find_key()
            obj.CreateAlphabet()
            res_message = obj.encr()
            return render_template('TritemiusPage.html',my_data1=res_message)
        elif 'form2'in request.form:
            decr_text = request.form['TextDecr']
            if len(request.form['InpKey4']) != 0:
                input_array.append(request.form['InpKey4'])

            elif len(request.form['InpKey51']) != 0:
                if len(request.form['InpKey52']) != 0:
                    input_array.extend((int(request.form['InpKey51']),int(request.form['InpKey52'])))
                else:
                    return render_template('TritemiusPage.html',er_info2=eror)

            else:
                if len(request.form['InpKey61']) != 0 and len(request.form['InpKey62']) != 0 and len(request.form['InpKey63']) != 0:
                    input_array.extend((int(request.form['InpKey61']),int(request.form['InpKey62']),int(request.form['InpKey63'])))
                else:
                    return render_template('TritemiusPage.html',er_info2=eror)

            obj = TritemiusChifr(decr_text, input_array)
            obj.find_key()
            obj.CreateAlphabet()
            res_message = obj.decr()
            return render_template('TritemiusPage.html', my_data2=res_message)

    return render_template('TritemiusPage.html')


class EncryptMessage():
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



class TritemiusChifr(EncryptMessage):
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
            # print(self.arr_of_keys)
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


if __name__ == '__main__':
    app.run(debug=True)
