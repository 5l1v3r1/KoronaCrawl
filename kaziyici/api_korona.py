# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

#---------------------------------------#
from flask import Flask                 #
from flask import jsonify,make_response #
from flask import request               #
from flask import send_from_directory   #
#---------------------------------------#
from kaziyici.scrape_korona import sozluk
#---------------------------------------#

#-----------------------#
app = Flask(__name__)   #
#-----------------------#

hata = {'HATALI İSTEK!' : 'Aradığınız içerik mevcut değil. Lütfen isteğinizi kontrol edin.'}

@app.route('/koronaVerileri', methods=['GET'])
def koronaVerileri():
    return jsonify(sozluk)

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(directory=app.root_path, filename='favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify(hata), 404)

#---------------------------------------------------#
if __name__ == '__main__':                          #
    app.config['JSON_AS_ASCII'] = False             #
    app.run(debug=True, host='0.0.0.0', port=5000)  #
#---------------------------------------------------#