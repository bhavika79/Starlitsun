from flask import Flask, render_template, request, redirect
import mysql.connector
import os

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
def dashboard():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")
    products = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM customers")
    customers = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM orders")
    orders = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return render_template(
        "dashboard.html",
        products=products,
        customers=customers,
        orders=orders
    )


@app.route("/add-product")
def add_product_page():
    return render_template("add_product.html")


@app.route("/add-product", methods=["POST"])
def add_product():

    name = request.form["name"]
    price = request.form["price"]

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO products(name,price) VALUES(%s,%s)",
        (name, price)
    )

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


@app.route("/customers")
def customers():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "customers.html",
        customers=customers
    )


@app.route("/orders")
def orders():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders")

    orders = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "orders.html",
        orders=orders
    )
@app.route("/inventory-reports")
def inventory_reports():

    conn = get_connection()

    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT *
        FROM inventory_reports
        ORDER BY generated_at DESC
        """
    )

    reports = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "inventory_reports.html",
        reports=reports
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )