from flask import Flask,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
from word_extraction import extraction
from database import db
@app.route("/information/get_information_list")
def get_information_list():
    information_list = []
    for information in db.get_all_information():
        information_list.append({
            'id': information[0],
            'name': information[1],
            'content':information[2]
        })
    return  information_list

@app.route("/information/remove_all_audio_information")
def remove_all_audio_information():
    db.remove_all_audio_information()
    return {}

@app.route("/information/get_audio_list")
def get_audio_list():
    extraction.save_audio_list()
    return get_information_list()

@app.route("/information/extract_content_audio", methods=['POST'])
def extract_content_audio():
    content = extraction.extract_content_words_by_id(request.json.get('id'))
    return {"content":content}

if __name__ == '__main__':
    app.run()
