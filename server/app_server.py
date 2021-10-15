import os
import yaml
from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

with open('../data/data.yml', 'r') as file:
    data = yaml.safe_load(file)
with open('../data/booked_items.yml', 'r') as file:
    users = yaml.safe_load(file)


@app.route("/post-users", methods=['POST'])
def reserve():
    user, item = request.form.get('username'), request.form.get('item')
    if not user:
        return 'authorization error'
    if not item:
        return 'item was not provided'

    user_data = users.get(user, {})
    user_data[item] = user_data.get(item, 0) + 1
    users[user] = user_data
    return make_response(users)


@app.route("/post-data", methods=['POST'])
def reserve_data():
    item = request.form.get('item')
    data[item] -= 1
    return make_response(data)


@app.route("/get-data", methods=['GET'])
def get_data():
    return make_response(data)


@app.route("/get-stats", methods=['GET'])
def get_stats():
    user = request.form.get('username')
    user_data = users.get(user, {})
    users[user] = user_data
    return make_response(users)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

