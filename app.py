from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from word_extraction import extraction
from database import db
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/information/get_information_list")
def get_information_list():
    print(db.get_all_information())
    information_list = []
    for information in db.get_all_information():
        information_list.append({
            'name': information[1],
            'content':information[2]
        })
    return  information_list

app.run()
