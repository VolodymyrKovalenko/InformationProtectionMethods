from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import string
import re
import os
from Crypto.Cipher import DES

from TritemiusModule import TritemiusChifr
from CaesarModule import CaesarChifr
from GamblingModule import GamblingChifr
from BookingChifrModule import BookingChifr
from BackpackModule import BackpackChifr

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
    if request.method == 'POST':
        input_array = []
        input_text = request.form['InpText']
        radio_option = request.form.get('trt_radio')
        if radio_option == 1:
            input_array.append(request.form['InpKey'])

        elif radio_option == 2:
            input_array.extend((int(request.form['InpKey1']), int(request.form['InpKey2'])))

        else:
            input_array.extend((int(request.form['InpKey31']), int(request.form['InpKey32']), int(request.form['InpKey33'])))

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

@app.route('/des_aes',methods=['GET','POST'])
def des_aes_app():
    if request.method == 'POST':
        input_text = request.form['InpText']
        input_key = request.form['InpKey']
        iv = request.form['init_vector']
        input_des_method = request.form.get('des_method')
        mode_option = {
            'ECB': DES.MODE_ECB,
            'CBC': DES.MODE_CBC,
            'CFB': DES.MODE_CFB,
            'OFB': DES.MODE_OFB,
            'CTR': DES.MODE_CTR
        }
        try:
            des_mode = mode_option[input_des_method]
        except KeyError:
            des_mode = None
        try:
            obj = DES.new(input_key, des_mode,iv)
        except ValueError:
            return render_template('DesChifr.html', data_encr='Key and initialization vector must be 8 bytes long')

        if 'encr_form' in request.form:
            try:
                res_message = obj.encrypt(input_text)
            except ValueError:
                return render_template('DesChifr.html',data_encr='Input strings must be a multiple of 8 in length. Length {} instead.'.format(len(input_text)))

            res_message = res_message.decode("latin-1")
            return render_template('DesChifr.html', data_encr=res_message)
        elif 'decr_form' in request.form:
            input_text = input_text.encode("latin-1")
            try:
                res_message = obj.decrypt(input_text)
            except ValueError:
                return render_template('DesChifr.html',data_decr = 'Input strings must be a multiple of 8 in length. Length {} instead.'.format(len(input_text)))
            res_message = res_message.decode("latin-1")
            return render_template('DesChifr.html',data_decr=res_message)
    return render_template('DesChifr.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/backpack', methods=['GET', 'POST'])
def backpack_app():
    if request.method == 'POST':
        if 'encr_form' in request.form:
            text = request.form['InpText']
            open_key = request.form['OpenKey']
            obj = BackpackChifr(text,None,None,None,open_key)
            res_message = obj.encr()

            return render_template('BackpackChifrPage.html', data_encr=res_message)
        elif 'decr_form' in request.form:
            text = request.form['InpText']
            private_key = request.form['InpKey']
            m = int(request.form['InpKeyM'])
            t = int(request.form['InpKeyT'])
            obj = BackpackChifr(text,private_key, m, t, None)
            res_message = obj.decr()

            return render_template('BackpackChifrPage.html', data_decr=res_message)
    return render_template('BackpackChifrPage.html')


if __name__ == '__main__':
    app.run(debug=True)
