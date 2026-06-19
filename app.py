from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


db = mysql.connector.connect(
host="localhost",
user="root",
password="rahulg0768",
database="portfolio_db"
)

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

     name = request.form["name"]
     email = request.form["email"]
     message = request.form["message"]

     cursor = db.cursor()

     sql = """
     INSERT INTO contacts (name, email, message)
     VALUES (%s, %s, %s)
     """

     values = (name, email, message)

     cursor.execute(sql, values)
     db.commit()

     cursor.close()

     return redirect("/contact")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)