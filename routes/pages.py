# routes/pages.py
from flask import Blueprint, render_template, request, redirect, url_for, flash

# Create the blueprint object
pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("index.html")

@pages.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        employee_id = request.form.get("employee_id")
        password = request.form.get("password")
        
        print(f"Username: {username}")
        print(f"Employee ID: {employee_id}")
        print(f"Password: {password}")
        
        flash("Login successful!") 
        return redirect(url_for("pages.home")) # Note: changed to pages.home
        
    return render_template("login.html")

@pages.route("/about")
def about():
    return render_template("about.html")

@pages.route("/contact")
def contact():
    return render_template("contact.html")