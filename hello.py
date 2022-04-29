from flask import Flask,render_template, request

import json
from werkzeug.utils import secure_filename
# from requests import request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your-url')
def your_url():
    urls ={}

    if 'url'in request.args.keys():
     urls[request.args['code']]={'url':request.args['url']}
    else:
        f=request.files['file']
        full_name=request.args['code'] +secure_filename(f.filename)
        f.save('/home/moringa/Documents/flask/' + full_name)
        urls[request.args['code']]={'file':full_name}
    with open('urls.json','w') as url_file:
        json.dump(urls,url_file) 
    return render_template('your_url.html',code=request.args['code'])

@app.route('/<string:code>')
def redirect_to_url(code):
    