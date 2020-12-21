import logging
from uuid import uuid4
from flask import Flask, request, jsonify
# from flask_cors import CORS


app = Flask(__name__)
# CORS(app)


@app.route('/test/json', methods=["GET", "POST"])
def test_json():
    request_id = uuid4()
    try:
        return jsonify({'requestId': request_id, 'message': 'success', 'contentType': request.headers.get('Content-Type'), 'body': request.json})
    except Exception as e:
        logging.error(e)
        return jsonify({'requestId': request_id, 'message': 'failed', 'contentType': '', 'body': {}}), 400


@app.route('/test/json/<path_var>', methods=["GET", "POST"])
def test_json_var(path_var):
    request_id = uuid4()
    try:
        path_var = request.view_args.get("path_var")
        return jsonify({'pathVariable': path_var, 'requestId': request_id, 'message': 'success', 'contentType': request.headers.get('Content-Type'), 'body': request.json})
    except Exception as e:
        logging.error(e)
        return jsonify({'pathVariable': path_var, 'requestId': request_id, 'message': 'failed', 'contentType': '', 'body': {}}), 400


@app.route('/post/json', methods=["POST"])
def post_json():
    request_id = uuid4()
    try:
        print(" body >>>>>>")
        print(request.json)
        return jsonify({'requestId': request_id, 'message': 'success', 'contentType': request.headers.get('Content-Type'), 'body': request.json})
    except Exception as e:
        logging.error(e)
        return jsonify({'requestId': request_id, 'message': 'failed', 'contentType': '', 'body': {}}), 400


@app.route('/post/form', methods=["POST"])
def post_form():
    request_id = uuid4()
    try:
        body = {'TotalFiles': len(request.files)}
        # for k, v in dict(request.files).items():
        #     body[k] = v.filename + "(" + v.mimetype + ")"
        body.update(request.form.to_dict())
        return jsonify({'requestId': request_id, 'message': 'success', 'contentType': request.headers.get('Content-Type'), 'body': body})
    except Exception as e:
        logging.error(e)
        return jsonify({'requestId': request_id, 'message': 'failed', 'contentType': '', 'body': {}}), 400


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
