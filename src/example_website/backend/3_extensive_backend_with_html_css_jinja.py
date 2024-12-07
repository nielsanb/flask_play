from flask import Flask
from flask import render_template

app = Flask(__name__)

### 1. Adding content to the .html via a jinja variable {{ variable }}
### A. Adding it inside the render_template() function
### B. See the html file for the {{ variable_to_pass }}
@app.route("/")
def function_passing_data_to_add_to_html_via_jinja_variable():
    return render_template("1_passing_data_to_html_via_jinja.html", variable_to_pass="content we added via passing the variable into a jinja block!")

### 2. Adding content to .html by passing a list!
### A. Same idea, but now with a list
### B. See the html file for the {{ for name in list_to_pass }}
@app.route("/list/")
def function_passing_list():
    return render_template("1_passing_data_to_html_via_jinja.html", list_to_pass=['maxime', 'stan', 'athanasios', 'erik', 'charlotte', 'niels'])

### 3. Template inheritance
### A. with in the base blocks: {% block name %} {% endblock %}
### B. and in the child {% extends from "base.html"%} and {% block name %} content of the block {% endblock %}
@app.route("/child/")
def child():
    return render_template("2_child.html")

### 4. Using CSS
### A. Note that, like with a normal website, if you'd include more files via the main document with a link, it creates another GET request.
### B. Stylesheets can be added via a <link>.
### C. For flask specifically, it will look in a directory called 'static' that is at the same level as the templates directory.
@app.route("/html_with_css/")
def with_css():
    return render_template("3_index_with_css.html")

### 5. Using bootstrap (css framework)
### A. Bootstap can also be added via links, that can be copied from their website: https://getbootstrap.com/docs/4.3/getting-started/introduction/
### B. The CSS should be within the header, but the js could be better at the bottom of the body
### C. Note now in the developers tab, that we call to an external website!
@app.route("/base_with_bootstrap/")
def with_bootstrap():
    return render_template("4_base_with_bootstrap.html")

### 6. Bootstrap NAVbar
### A. Navbar code copied from bootstap website (I dont know either), just to demontrate the reusability of key-elements of the website
### B. with a base
### C. and a child
@app.route("/base_with_navbar/")
def with_navbar():
    return render_template("4_base_with_navbar.html")

@app.route("/child_with_navbar/")
def with_navbar2():
    return render_template("4_child_with_navbar.html")


if __name__ == "__main__":
    app.run(debug=True)

