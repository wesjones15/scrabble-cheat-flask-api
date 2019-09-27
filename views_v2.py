from findScrabbleWordsFromLetters import getScrabbleWordsFromLetters
from getBestScoringWords import getBestScoringWords

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def apiStatus():
    return "Scrabble Cheat API is running"

@app.route("/words/<letters>", methods=["GET","POST"])
def returnWords(letters):
    # letters = list(request.get_json(force=True).get('letters'))
    print(letters)
    word_list = getScrabbleWordsFromLetters(letters)
    print(len(word_list))
    best_words = getBestScoringWords(word_list)
    print(best_words)
    return jsonify({'words': best_words})
    
# I want to POST letters as JSON object to server
# I want to return best words object as JSON in response

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0',port=5000)