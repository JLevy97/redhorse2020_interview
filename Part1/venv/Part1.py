from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests, socket
from datetime import datetime
app = Flask(__name__)

nickname = False;

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/preview', methods = ['POST'])
def preview():
    name = request.form["nm"]
    cert = request.form["cert"]
    certDes = request.form["certDes"]
    date = request.form["date"]
    L = request.form["layout"]

    if(nickname == True):
        name = request.form["nnm"]

    if(L == 'Layout1'):
        return render_template('cert.html', a = name, c = cert, d = certDes, e = date)
    else:
        return render_template('cert2.html', a = nickname, c = cert, d = certDes, e = date)

@app.route('/submit', methods = ['POST'])
def submit():

    data = {}

    data['name'] = request.form["nm"]
    data['nickname'] = request.form["nnm"]
    data['cert'] = request.form["cert"]
    data['certDes'] = request.form["certDes"]
    data['date'] = request.form["date"]
    data['layout'] = request.form["layout"]

    data['reqT'] = datetime.now()
    hostname = socket.gethostname()
    data['ip'] = socket.gethostbyname(hostname)

    j = jsonify(data)

    #result = requests.post("127.0.0.1:5001",data) #the rest Request for the back end storage micro-service.
                                            # IP and port should be swapped with whatever the microservice is running on

    return redirect(url_for("home"))

@app.route('/settings')
def settings():

    return render_template('sett.html')

@app.route('/update', methods = ['POST'])
def update():

    option = request.form["option"]
    print(option)

    if(option == 'yes'):
        print("in")
        nickname=True
    else:
        nickname=False

    return redirect(url_for("home"))

@app.route('/sr')
def sr():
    return "these are stored in another microservice"