from flask import Flask
from flask import request, render_template
from flask import make_response

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("0_index.html")

@app.route("/set_my_cookie/")
def new_cookie():
    response = make_response(render_template('2_child.html', foo=42))
    response.headers['X-Wieiscool'] = 'Niels is cool'
    response.set_cookie("hoecool", "heeeeel cool", max_age=30)
    return response

@app.route("/get_my_cookie/")
def get_cookie():
    if "hoecool" in request.cookies:
        hoecool = request.cookies["hoecool"]
        return f"Het cookie zeg dat niels {hoecool} is"
    else:
        return f"No cookie to display"

if __name__ == "__main__":
    app.run(debug=True)