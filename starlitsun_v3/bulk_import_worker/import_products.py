import csv
import os
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

with open("/app/products.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:

        cursor.execute(
            """
            INSERT INTO products
            (name, category, price)

            VALUES (%s,%s,%s)
            """,
            (
                row["name"],
                row["category"],
                row["price"]
            )
        )

conn.commit()

cursor.close()
conn.close()

print("Bulk Import Completed")