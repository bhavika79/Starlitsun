import os
import mysql.connector

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = conn.cursor()

cursor.execute(
"""
SELECT COUNT(*)
FROM products
"""
)

total = cursor.fetchone()[0]

cursor.execute(
"""
SELECT COUNT(*)
FROM products
WHERE category='Craft'
"""
)

craft = cursor.fetchone()[0]

cursor.execute(
"""
SELECT COUNT(*)
FROM products
WHERE category='Art'
"""
)

art = cursor.fetchone()[0]

cursor.execute(
"""
INSERT INTO inventory_reports
(
total_products,
craft_products,
art_products
)
VALUES(%s,%s,%s)
""",
(total, craft, art)
)

conn.commit()

cursor.close()
conn.close()

print("Inventory Report Created")