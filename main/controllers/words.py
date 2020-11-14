import random

from flask import jsonify, request
from strgen import StringGenerator

from main.app import app
from main.models.word import WordModel
from main.models.unit import UnitModel


@app.route('/words', methods=['GET'])
def get_words():
    """Returns 300 random words based on query's mode."""

    mode = request.args.get('mode', 'basic')

    if mode == 'basic':
        size = 200
        collection = WordModel.query.limit(size)
        words = [collection[random.randint(0, size-1)].value for i in range(300)]
        return jsonify(words), 200
    elif mode == 'numerical':
        words = []
        size = 18
        collection = UnitModel.query.all()
        for i in range(300):
            prefix = str(random.randint(1, 1000))
            suffix = str(collection[random.randint(0, size-1)].value)
            words.append(prefix + suffix)
        return jsonify(words), 200
    elif mode == 'random':
        words = []
        for i in range(300):
            words.append(StringGenerator('[\w\p\d]{'f'{random.randint(1, 8)}''}').render())
        return jsonify(words), 200
