#!/usr/bin/python3

from flask import Flask, request, jasonify
from functools import wraps

app = Flask(__name__)

def check_card(f):
    data = request.get_json()
    if not data.get("status"):
        response = {"approved":False,
        "newLimit":data.get("limit"),
        "reason":"Blocked Card"}
        return jasonify(response)

    if data.get("limit") < data.get("transaction").get("amount"):
        response = {"approved":False,
        "newLimit":data.get("limit"),
        "reason":"Transaction avove the limit"}
        return jasonify(*args, **kwargs)

    return(validation)

@app.route("/api/transactioni", methods=["POST"])
@check_card

def transaction():
    card = request.get_json()
    new_limit = card.get("limit")
    card.get("transaction").get("amount")
    response = {"approved":True,
    "newLimit":new_limit}
    return jasonify(response)

if __name__ == '__main__':
    app.run(debug=True)

