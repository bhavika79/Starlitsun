CREATE DATABASE IF NOT EXISTS starlitsun;

USE starlitsun;

CREATE TABLE IF NOT EXISTS products
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price INT
);

CREATE TABLE IF NOT EXISTS customers
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS orders
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100)
);


ALTER TABLE products
ADD COLUMN category VARCHAR(50);

CREATE TABLE IF NOT EXISTS inventory_reports
(
    id INT AUTO_INCREMENT PRIMARY KEY,

    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    total_products INT,

    craft_products INT,

    art_products INT
);

INSERT INTO products(name, category, price)
VALUES

('Handmade Greeting Card', 'Craft', 100),

('Paper Flower Bouquet', 'Craft', 150),

('Decorative Lantern', 'Craft', 300),

('Canvas Painting', 'Art', 500),

('Portrait Sketch', 'Art', 400),

('Watercolor Landscape', 'Art', 600);