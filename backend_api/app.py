from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)

# In-memory storage
products = {}
next_id = 1  # Auto-increment
products = {"id": 0, "name": "Product 0", "price": 0.0}


# Endpoint to retrieve all products or a single product by ID
@app.route("/products", methods=["GET"])
def get_products():
    product_id = request.args.get("id")
    if product_id:
        product = products.get(int(product_id))
        if not product:
            return jsonify({"error": "Product not found"}), 404
        return jsonify(product)
    return jsonify(list(products.values()))

# Endpoint to add a new
@app.route("/products", methods=["POST"])
def add_product():
    global next_id
    data = request.json
    if not data or not data.get("name") or not data.get("price"):
        return jsonify({"error": "Invalid input"}), 400

    product = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"],
    }
    products[next_id] = product
    next_id += 1
    return jsonify(product), 201

# Endpoint to update an existing item in memory
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    product["name"] = data.get("name", product["name"])
    product["price"] = data.get("price", product["price"])
    return jsonify(product)

# Endpoint to delete an item
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in products:
        return jsonify({"error": "Product not found"}), 404

    del products[product_id]
    return jsonify({"message": "Product deleted"}), 200

# Main/Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
