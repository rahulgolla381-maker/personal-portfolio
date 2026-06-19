from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)