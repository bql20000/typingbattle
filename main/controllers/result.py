from flask import jsonify

from main.app import app
from main.helpers import load_request_data
from main.models.result import ResultModel
from main.models.user import UserModel
from main.schemas.result import ResultSchema
from main.security import requires_auth


@app.route('/results', methods=['POST'])
@requires_auth
@load_request_data(ResultSchema)
def save_result(data, user_id):
    """Create a result record in database"""
    result = ResultModel(**data, user_id=user_id)
    result.save_to_db()
    return jsonify({}), 201


@app.route('/results', methods=['GET'])
@requires_auth
def get_result(user_id):
    """Return an user's statistics"""
    user = UserModel.query.get(user_id)
    results = user.results
    time_practiced = sum(r.time for r in results) if results else 0
    overall_wpm = (sum(r.wpm for r in results) / len(results)) if results else 0
    overall_acc = (sum(r.accuracy for r in results) / len(results)) if results else 0
    recent_wpm = (sum(r.wpm for r in results[:3]) / min(3, len(results))) if results else 0
    recent_acc = (sum(r.accuracy for r in results[:3]) / min(3, len(results))) if results else 0
    return jsonify(username=user.username,
                   time_practiced=time_practiced,
                   overall_wpm=overall_wpm,
                   overall_acc=overall_acc,
                   recent_acc=recent_acc,
                   recent_wpm=recent_wpm), 200
