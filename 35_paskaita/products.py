from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
products = [
        {'id': 1, 'label': 'Milk', 'price': 2.50 },
        {'id': 2, 'label': 'Bread', 'price': 1.49 },
        {'id': 3, 'label': 'Beer', 'price': 1.29 },
        {'id': 4, 'label': 'Cheese', 'price': 1.59 },
        {'id': 5, 'label': 'Eggs', 'price': 2.89 }
    ]
@app.route('/api/products', methods= ['GET', 'POST'])
def handle_products():
    if not request.method == 'POST':
        return jsonify(products)
    new_product = request.get_json()
    new_product['id'] = len(products) + 1
    products.append(new_product)
    return jsonify(new_product), 201


app.run(port=5000)