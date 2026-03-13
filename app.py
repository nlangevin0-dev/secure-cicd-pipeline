from flask import Flask, request
import os

app = Flask(__name__)

SECRET_KEY = "supersecretpassword123"

@app.route("/")
def home():
    return "Hello World"

@app.route("/search")
def search():
    query = request.args.get("q")
    result = os.popen(f"grep -r {query} /data").read()
    return result

if __name__ == "__main__":
    app.run(debug=True)