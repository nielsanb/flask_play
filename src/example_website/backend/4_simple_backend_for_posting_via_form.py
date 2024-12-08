from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def homepage():
    if request.method == "POST":
        name = request.form["name"]
        print(name) #zie terminal
        return f"the name I catched was {name}"

    return render_template("5_form.html")

if __name__ == '__main__':
    app.run(debug=True)