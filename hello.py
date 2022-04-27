from flask import Flask,render_template, request
import json
# from requests import request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/your-url')
def your_url():
    urls ={}
    urls[request.args['code']]={'url':request.args['url']}
    with open('urls.json','w') as url_file:
        json.dump(urls,url_file) 
    return render_template('your_url.html',code=request.args['code'])
