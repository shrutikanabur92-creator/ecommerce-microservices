from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Payment Service is running"

@app.route('/pay', methods=['POST'])
def payment():

    data = request.get_json()

    if not data or not data.get('amount'):
        return jsonify({"error": "Amount is required"}), 400

    return jsonify({
        "payment_status": "SUCCESS",
        "amount": data["amount"],
        "message": "Payment completed successfully"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
