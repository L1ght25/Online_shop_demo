
from flask import Flask, make_response, request

app = Flask(__name__)

# это должно быть в конфигурационном файле
data = {1: 100, 2: 200}
users = {}


@app.route("/api/reserve", methods=['POST'])
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


@app.route("/api/stats", methods=['GET'])
def stats():
    return make_response(
        {
            'user': {
                'name': 'kate', 'items': [{'item_id': '1', 'count': 5}, {'item_id': '2', 'count': 5}]
            }
        }
    )


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8000', debug=True)