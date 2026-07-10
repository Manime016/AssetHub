from flask import Blueprint, render_template

pages = Blueprint("pages", __name__)


@pages.route("/")
def home():
    return render_template("login.html")

@pages.route("/dashboard")
def dashboard():
    return render_template("index.html")

@pages.route("/login")
def login():
    return render_template("login.html")


@pages.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")


@pages.route("/about")
def about():
    return render_template("about.html")


@pages.route("/contact")
def contact():
    return render_template("contact.html")


@pages.route("/add_employee")
def add_employee():
    return render_template("add_employee.html")


@pages.route("/employee_list")
def employee_list():
    return render_template("employee_list.html")


@pages.route("/add_asset")
def add_asset():
    return render_template("add_asset.html")