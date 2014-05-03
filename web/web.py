import os

from decimal import Decimal
from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

from scripts.varita import process


app = Flask(__name__)

UPLOAD_FOLDER = '/tmp'
ALLOWED_EXTENSIONS = ['csv']
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = UPLOAD_FOLDER

app.debug = True


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        # POST request
        form = request.form
        f = request.files['csv']
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            finput = os.path.join(
                app.config['UPLOAD_FOLDER'],
                filename)
            foutput = os.path.join(
                app.config['RESULT_FOLDER'],
                filename)
            f.save(finput)

        process('Name Goes Here', finput, foutput,
                Decimal(form['blanco']),
                Decimal(form['vol_muestra']),
                int(form['prec']))

        return render_template('done.html', filename=filename)


@app.route('/result/<filename>')
def get_resuls(filename):
    return send_from_directory(
        app.config['RESULT_FOLDER'],
        filename)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
