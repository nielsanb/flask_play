from flask import Flask
from flask import render_template

app = Flask(__name__)

### Please note that (for flask specifically) the templates folder should actually be named 'templates'
### AND should be sitting next to the python file
### Please also note that a simple html structure can be made by only typing '!' and enter, in a .html file
@app.route("/")
def home():
    return render_template("0_index.html")

if __name__ == "__main__":
    app.run(debug=True)


