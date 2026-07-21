from flask import Flask, request, jsonify
import mysql.connector
import os
import time

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


@app.route("/")
def home():
    return {
        "application": "StarlitSun",
        "status": "running"
    }


# ==========================
# PRODUCTS
# ==========================

@app.route("/products", methods=["POST"])
def add_product():

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products(name, price) VALUES(%s,%s)",
        (data["name"], data["price"])
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Product Added"}


@app.route("/products", methods=["GET"])
def get_products():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(products)


# ==========================
# CUSTOMERS
# ==========================

@app.route("/customers", methods=["POST"])
def add_customer():

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO customers(name,email) VALUES(%s,%s)",
        (data["name"], data["email"])
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Customer Added"}


@app.route("/customers", methods=["GET"])
def get_customers():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(customers)


# ==========================
# ORDERS
# ==========================

@app.route("/orders", methods=["POST"])
def add_order():

    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO orders(customer_name, product_name) VALUES(%s,%s)",
        (data["customer_name"], data["product_name"])
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Order Added"}


@app.route("/orders", methods=["GET"])
def get_orders():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders")

    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(orders)


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
