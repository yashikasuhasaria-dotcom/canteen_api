from flask import Flask,render_template ,jsonify, request

app = Flask(__name__)

menu = {"Poha": 30, "Tea": 15, "Sandwich": 50}


@app.route("/menu")
def get_menu():
    return render_template("index.html")


@app.route("/order", methods=["POST"])
def place_order():
    order = request.get_json()

    item = order["item"]
    qty = order["quantity"]

    total = menu[item] * qty

    return jsonify({
        "order_id": 101,
        "total": total,
        "status": "Order Placed"
    })


app.run(host="0.0.0.0" , port=5001)
