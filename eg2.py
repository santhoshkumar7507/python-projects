from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    numbers = [10, 20, 30, 40, 50]
    return render_template("index.html", content=numbers)

if __name__ == "__main__":
    app.run(debug=True)
