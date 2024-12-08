from flask import Flask, redirect, url_for, render_template, request
from flask import session
from datetime import timedelta

app = Flask(__name__)

##All session data, from the imported session object, is stored encrypted at the server.
##To encrypt an decrypt data, you need to set a secret key!
app.secret_key = "difficultsecretkey"

###Sessions are stored in a temporary directory at the server.
###You can either let the sessions be deleted if a tab is closed
###, or you can make it permanent (i.e. over multiple tabs) and for a specific length of time.
app.permanent_session_lifetime = timedelta(seconds=20) #or minutes, hours, days etc.
# Note the session.permanent = True in the function!

###Note that however we call the session permantent, then are designed to use
###for temporary only. NEVER STORE (SENSITIVE) DATA FOR REAL PERMINANTLY IN THE SESSION
###You would do that in a database, and than read it from there!
@app.route("/")
def home():
    return render_template("0_index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["user_name"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("6_login.html")
    
@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"Hello user: {user}"   
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)