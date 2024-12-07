from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Hello!</h1> This is my page!"

if __name__ == "__main__":
    app.run()