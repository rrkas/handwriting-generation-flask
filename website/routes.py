import io
import os
import uuid

import pywhatkit as kit
from flask import *

from website import app

output_dir = os.path.join('website', 'static', 'output')
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

allowed_file_ext = ['txt']


def allowed_file(filename):
    return filename.split('.')[-1] in allowed_file_ext


def generate_signature(file):
    try:
        output_filename = str(uuid.uuid4().hex)
        file.save(os.path.join(output_dir, output_filename + '.txt'))
        with open(os.path.join(output_dir, output_filename + '.txt'), 'r') as f:
            text = f.read()
        os.remove(os.path.join(output_dir, output_filename + '.txt'))
        kit.text_to_handwriting(
            string=text,
            rgb=(0, 0, 0),
            save_to=os.path.join(output_dir, output_filename + '.png'),
        )
        return output_filename, True
    except BaseException as e:
        print(e)
        return str(e), False


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part!')
            return redirect(request.url)
        file = request.files.get('file')
        if not allowed_file(file.filename):
            flash('Invalid File!')
            return redirect(request.url)
        img_name, valid = generate_signature(file)
        if valid:
            flash('Images Converted Successfully!', 'success')
        else:
            flash('Something went wrong! Please try again!!', 'error')
            return redirect(request.url)
        return redirect(url_for('home', img_name=img_name))
    filename = request.args.get('img_name')
    result_path = os.path.join(output_dir, str(filename) + '.png')
    if filename and not os.path.exists(result_path):
        abort(404)
    return render_template('home.html', img_name=request.args.get('img_name'))


@app.route('/download/<string:filename>', methods=['GET', 'POST'])
def download(filename):
    result_path = os.path.join(output_dir, filename + '.png')
    if not os.path.exists(result_path):
        abort(404)

    return_data = io.BytesIO()
    with open(result_path, 'rb') as fo:
        return_data.write(fo.read())
    return_data.seek(0)

    os.remove(result_path)

    return send_file(
        return_data,
        mimetype='image/png',
        as_attachment=True,
        attachment_filename='txt2handwriting.png'
    )


@app.errorhandler(404)
def error_400(error):
    return render_template('errors/404.html')
