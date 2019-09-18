from findScrabbleWordsFromLetters import getScrabbleWordsFromLetters
from getBestScoringWords import getBestScoringWords

from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def apiStatus():
    return "Scrabble Cheat API is running"

@app.route("/words", methods=["POST"])
# @cross_origin()
def returnWords():
    letters = list(request.get_json().get('letters'))
    print(letters)
    word_list = getScrabbleWordsFromLetters(letters)
    best_words = getBestScoringWords(word_list)
    return jsonify({'words': best_words})
    
# I want to POST letters as JSON object to server
# I want to return best words object as JSON in response

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)