from flask import jsonify, request

from main import app
from main.models.word import WordModel


@app.route('/words', methods=['GET'])
def get_words():
    """Returns a collection of common words
    (rank from the most common to the least).
    """
    size = request.args.get('size', 200)
    words = WordModel.query.limit(size)
    return jsonify([word.value for word in words]), 200
