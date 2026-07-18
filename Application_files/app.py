from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "store": "StarlitSun",
        "message": "Welcome to StarlitSun"
    }

@app.route("/crafts")
def crafts():
    return {
        "category": "Crafts",
        "products": [
            "Handmade Greeting Card",
            "Paper Flowers",
            "Decorative Lantern"
        ]
    }

@app.route("/arts")
def arts():
    return {
        "category": "Arts",
        "products": [
            "Canvas Painting",
            "Abstract Artwork",
            "Sketch Portrait"
        ]
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)