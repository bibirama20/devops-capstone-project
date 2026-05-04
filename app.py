from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = []
counter = 1

# HOME (biar tidak Not Found)
@app.route('/')
def home():
    return "API is running"

# CREATE
@app.route('/accounts', methods=['POST'])
def create_account():
    global counter
    data = request.get_json()

    if not data:
        return jsonify({"message": "No input data"}), 400

    account = {
        "id": counter,
        "name": data.get("name"),
        "email": data.get("email"),
        "address": data.get("address"),
        "phone_number": data.get("phone_number")
    }
    accounts.append(account)
    counter += 1
    return jsonify(account), 201

# LIST
@app.route('/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts)

# READ
@app.route('/accounts/<int:id>', methods=['GET'])
def get_account(id):
    for acc in accounts:
        if acc["id"] == id:
            return jsonify(acc)
    return jsonify({"message": "Not found"}), 404

# UPDATE
@app.route('/accounts/<int:id>', methods=['PUT'])
def update_account(id):
    data = request.get_json()
    for acc in accounts:
        if acc["id"] == id:
            acc["name"] = data.get("name", acc["name"])
            acc["email"] = data.get("email", acc["email"])
            acc["address"] = data.get("address", acc.get("address"))
            acc["phone_number"] = data.get("phone_number", acc.get("phone_number"))
            return jsonify(acc)
    return jsonify({"message": "Not found"}), 404
# DELETE
@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    global accounts
    accounts = [acc for acc in accounts if acc["id"] != id]
    return jsonify({"message": "Deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)