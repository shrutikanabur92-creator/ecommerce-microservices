from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Order Service is running"

@app.route('/orders', methods=['POST'])
def create_order():

    data = request.get_json()

    if not data or not data.get('product_id') or not data.get('quantity'):
        return jsonify({"error": "Product ID and quantity are required"}), 400

    product_response = requests.get(
        f"http://product-service:5001/products/{data['product_id']}"
    )

    if product_response.status_code != 200:
        return jsonify({"error": "Product not found"}), 404

    product = product_response.json()

    quantity = data["quantity"]

    if not isinstance(quantity, int) or quantity < 1:
        return jsonify({"error": "Quantity must be a positive integer"}), 400

    total = product["price"] * quantity

    payment_response = requests.post(
        "http://payment-service:5003/pay",
        json={"amount": total}
    )

    if payment_response.status_code != 200:
        return jsonify({"error": "Payment failed"}), 400

    payment = payment_response.json()

    return jsonify({
        "message": "Order placed successfully",
        "product": product["name"],
        "quantity": quantity,
        "total_amount": total,
        "payment_status": payment["payment_status"]
    }), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
