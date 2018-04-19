from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import string
import re

from TritemiusModule import TritemiusChifr
from CaesarModule import CaesarChifr
from GamblingModule import GamblingChifr
from BookingChifrModule import BookingChifr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def caesar_app():
    if request.method == 'POST':
        inp_text = request.form['InpText']
        input_key = int(request.form['InpKey'])
        obj = CaesarChifr(inp_text, input_key)
        obj.CreateAlphabet()
        if 'encr_form' in request.form:
            res_message = obj.encr()
            return render_template('MainPage.html', data_encr=res_message)
        elif 'decr_form' in request.form:
            res_message = obj.decr()
            return render_template('MainPage.html', data_decr=res_message)

    return render_template('MainPage.html')


@app.route('/tritemius', methods=['GET', 'POST'])
def tritemius_app():
    error = 'Enter all the fields'
    if request.method == 'POST':
        input_array = []
        input_text = request.form['InpText']
        if len(request.form['InpKey']) != 0:
            input_array.append(request.form['InpKey'])

        elif len(request.form['InpKey1']) != 0:
            if len(request.form['InpKey2']) != 0:
                input_array.extend((int(request.form['InpKey1']), int(request.form['InpKey2'])))
            else:
                return render_template('TritemiusPage.html', er_info=error)

        else:
            if len(request.form['InpKey31']) != 0 and len(request.form['InpKey32']) != 0 and len(
                    request.form['InpKey33']) != 0:
                input_array.extend(
                    (int(request.form['InpKey31']), int(request.form['InpKey32']), int(request.form['InpKey33'])))
            else:
                return render_template('TritemiusPage.html', er_info=error)

        obj = TritemiusChifr(input_text, input_array)
        obj.find_key()
        obj.CreateAlphabet()
        if 'encr_form' in request.form:
            res_message = obj.encr()
            return render_template('TritemiusPage.html', data_encr=res_message)
        elif 'decr_form' in request.form:
            res_message = obj.decr()
            return render_template('TritemiusPage.html', data_decr=res_message)

    return render_template('TritemiusPage.html')


@app.route('/gambling', methods=['GET', 'POST'])
def gambling_app():
    if request.method == 'POST':
        input_text = request.form['InpText']
        input_key = int(request.form['InpKey'])
        obj = GamblingChifr(input_text, input_key)
        obj.CreateAlphabet()
        obj.find_gambling_key()
        if 'encr_form' in request.form:
            res_message = obj.encr()
            return render_template('Gambling.html', data_encr=res_message)
        elif 'decr_form' in request.form:
            res_message = obj.decr()
            return render_template('Gambling.html', data_decr=res_message)
    return render_template('Gambling.html')

@app.route('/bookish',methods=['GET','POST'])
def bookish_app():
    if request.method == 'POST':
        input_text = request.form['InpText']
        input_key = request.form['InpKey']
        obj = BookingChifr(input_text,input_key)
        obj.split_booking_key()
        if 'encr_form' in request.form:
            res_message = obj.encr_booking()
            return render_template('BookishChifrPage.html', data_encr=res_message)
        elif 'decr_form' in request.form:
            res_message = obj.decr_booking()
            return render_template('BookishChifrPage.html', data_decr=res_message)

    return render_template('BookishChifrPage.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
