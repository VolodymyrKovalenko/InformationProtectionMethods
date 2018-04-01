from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import string
import re

from TritemiusModule import TritemiusChifr
from CaesarModule import CaesarChifr
from GamblingModule import GamblingChifr

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def firstPost():
    if request.method == 'POST':
        if 'form1' in request.form:
            encr_text = request.form['TextEncr']
            input_key = int(request.form['InpKey1'])
            obj = CaesarChifr(encr_text, input_key)
            obj.CreateAlphabet()
            res_message = obj.encr()
            return render_template('MainPage.html', my_data1=res_message)
        elif 'form2' in request.form:
            decr_text = request.form['TextDecr']
            input_key = int(request.form['InpKey2'])
            obj = CaesarChifr(decr_text, input_key)
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
                    input_array.extend((int(request.form['InpKey21']), int(request.form['InpKey22'])))
                else:
                    return render_template('TritemiusPage.html', er_info=eror)

            else:
                if len(request.form['InpKey31']) != 0 and len(request.form['InpKey32']) != 0 and len(
                        request.form['InpKey33']) != 0:
                    input_array.extend(
                        (int(request.form['InpKey31']), int(request.form['InpKey32']), int(request.form['InpKey33'])))
                else:
                    return render_template('TritemiusPage.html', er_info=eror)

            obj = TritemiusChifr(encr_text, input_array)
            obj.find_key()
            obj.CreateAlphabet()
            res_message = obj.encr()
            return render_template('TritemiusPage.html', my_data1=res_message)
        elif 'form2' in request.form:
            decr_text = request.form['TextDecr']
            if len(request.form['InpKey4']) != 0:
                input_array.append(request.form['InpKey4'])

            elif len(request.form['InpKey51']) != 0:
                if len(request.form['InpKey52']) != 0:
                    input_array.extend((int(request.form['InpKey51']), int(request.form['InpKey52'])))
                else:
                    return render_template('TritemiusPage.html', er_info2=eror)

            else:
                if len(request.form['InpKey61']) != 0 and len(request.form['InpKey62']) != 0 and len(
                        request.form['InpKey63']) != 0:
                    input_array.extend(
                        (int(request.form['InpKey61']), int(request.form['InpKey62']), int(request.form['InpKey63'])))
                else:
                    return render_template('TritemiusPage.html', er_info2=eror)

            obj = TritemiusChifr(decr_text, input_array)
            obj.find_key()
            obj.CreateAlphabet()
            res_message = obj.decr()
            return render_template('TritemiusPage.html', my_data2=res_message)

    return render_template('TritemiusPage.html')


@app.route('/gambling', methods=['GET', 'POST'])
def gambling():
    if request.method == 'POST':
        if 'form1' in request.form:
            encr_text = request.form['TextEncr']
            input_key = int(request.form['InpKey1'])
            obj = GamblingChifr(encr_text, input_key)
            obj.CreateAlphabet()
            obj.find_gambling_key()
            res_message = obj.encr()
            return render_template('Gambling.html', data_encr=res_message)
        elif 'form2' in request.form:
            decr_text = request.form['TextDecr']
            input_key = int(request.form['InpKey2'])
            obj = GamblingChifr(decr_text, input_key)
            obj.CreateAlphabet()
            obj.find_gambling_key()
            res_message = obj.decr()
            return render_template('Gambling.html', data_decr=res_message)
    return render_template('Gambling.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
