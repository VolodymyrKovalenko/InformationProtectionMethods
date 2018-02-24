from flask import Flask,render_template,request,redirect, url_for, jsonify, json
import string


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

if __name__ == '__main__':
    app.run(debug=True)
