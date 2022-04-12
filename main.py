from flask import Flask,request
import string


app = Flask(__name__)

@app.route('/<name>')
def user_name(name):
    return f"Welcome {name}"

if __name__ == "__main__":
    app.run(port=8080, debug=True)