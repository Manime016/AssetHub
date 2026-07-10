# routes/login.py
from flask import Blueprint, request, redirect, url_for, flash, render_template
from database.connection import get_db_connection
from database.login_queries import LoginQueries

login_bp = Blueprint("login", __name__)

# Helper validation function
def validate_input(username, employee_id, password):
    if not username or not employee_id or not password:
        flash("❌ All fields are required.", "danger")
        return False
    return True

@login_bp.route("/login-submit", methods=["POST"])
def login_submit():
    # Gather inputs from the form
    username = request.form.get("email")
    employee_id = request.form.get("employee_id")
    password = request.form.get("password")

    # Validate inputs
    if not validate_input(username, employee_id, password):
        return redirect(url_for("pages.login"))

    db_connection = get_db_connection() 
    login_queries = LoginQueries(db_connection)

    # Check if the employee exists and password matches
    if login_queries.verify_employee(employee_id, password):
        flash("✅ Login successful!", "success")
        return redirect(url_for("pages.dashboard"))
    else:
        flash("❌ Invalid credentials. Please try again.", "danger")
        return redirect(url_for("pages.login"))