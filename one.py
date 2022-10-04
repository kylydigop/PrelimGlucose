from flask import Flask, jsonify, request

import json

app = Flask(__name__)

glucose = [
    {
        "glucose_id": 1,
        "date" : "December/25/2011",
        "glucose" : "100mg"
    }
]

@app.route('/glucose', methods=['GET'])
def displayGlucose():
    return jsonify(glucose)

if __name__== '__main__':
    app.run()