from flask import Flask
from flask import redirect, url_for
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Hello!<h1> This is my page!"

# ----- URL DATA -----
### 1. Picking up a value from the URL
### A. from URL by <name>
### B. passing it automatically into the functions parameter (name):
### C. using the variable in an f-string.
@app.route("/user/<name>/") 
def user(name):
    return f"Hello {name}!"


# ----- QUERY STRING DATA -----
### 2. Picking up the QUERY STRING
### A. Note that we do not pass along data into the function
### B. Instead we pick it up (and set a vairable) via the requests function that we imported.
### C. using it in an f-string again.
### Z. Note that you could also, perhaps better, use request.args.get("name")
### See this working example: http://127.0.0.1:5000/send_a_query_string?name=niels&age=35
#Note that you get a bytestring!
@app.route("/send_a_query_string/")
def qstring():
    query_string = request.query_string
    name = request.args.get('name')
    return f'Query string that you send was: {query_string}, and the name was: { name }'

# ----- POST REQUEST DATA -----
### 3. Picking up data from a POST request (and putting it in a file)
### A. Note the methods=[] parameter makes that the server accepts POST data.
### B. request.json returns the parsed JSON data that is POSTED with the request.
### B2. The request must have the application/json content type! Or use request.get_json(force=True) to ignore the content type.
### B3. Note that you can set this with doing the request (see client/client_post.py)
### Z. Later we will use a FORM to send data: request.form
### Z. Note that these request.methods return a MultiDict or Json.
@app.route("/endpoint/", methods=["POST"])
def data_via_post():
    if request.method == "POST":
        json_data = request.json
        return f"Content received {json_data}"
    else:
        return "Method not allowed!"

# ----- COOKIE -----
### Cookie has been done in another file!


# ----- Redirection -----
### 4. Redirecting and incoming url
### A. Works via the imported functions 'redirect' and 'url_for'
### B. note that url_for does NOT point to a url, but the related function! 
### C. It does redirect you to the accoring url though.
@app.route("/admin/")
def admin():
    return redirect(url_for("name_of_function_that_we_are_redirecting_to")) #thus not a url!

@app.route("/redirection/of/the/admin")
def name_of_function_that_we_are_redirecting_to():
    return "We redirected the admin url to this function!"

### 5. Redirecting and incoming url AND passing the parameter along via a query string
#A. Note that in the first url, the data is picked from the url path by <admin_name>, and inserted automatically to the function parameter <admin_name>.
#B. But the send forward via a query string.
@app.route("/admin2/<admin_name>/")
def admin2(admin_name):
    return redirect(url_for("redirect_function", admin_name=admin_name)) 

#C. And that this query string can be read via requests
@app.route("/redirection/of/the/admin_with_parameter/")
def redirect_function():
    query_string = request.query_string
    return f"We redirected the admin url to this function! With {query_string}"



if __name__ == "__main__":
    app.run(debug=True)