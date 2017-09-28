
from flask import Flask 
from flask import jsonify, request
from flask import make_response
app = Flask(__name__)
import main 
import json

# test
@app.route("/")
def hello():
    print request.get_json()
    result = main.run_en_json()
    # return json.dumps(result)
    return jsonify(result)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)