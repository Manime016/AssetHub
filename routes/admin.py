from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.connection import get_db_connection
from database.admin_queries import AdminQueries

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin_management")
def admin_management():
    db = get_db_connection()
    admin_queries = AdminQueries(db)

    employees = admin_queries.get_all_employees()

    return render_template(
        "admin_management.html",
        employees=employees
    )


@admin_bp.route("/promote_admin", methods=["POST"])
def promote_admin():
    employee_id = request.form.get("employee_id")
    password = request.form.get("password")

    db = get_db_connection()
    admin_queries = AdminQueries(db)

    if admin_queries.promote_admin(employee_id, password):
        flash("Admin added successfully.", "success")
    else:
        flash("Employee is already an admin.", "danger")

    return redirect(url_for("admin.admin_management"))

@admin_bp.route("/remove_admin", methods=["POST"])
def remove_admin():

    employee_id = request.form.get("employee_id")

    db = get_db_connection()
    admin_queries = AdminQueries(db)

    if admin_queries.remove_admin(employee_id):
        flash("Admin removed successfully.", "success")
    else:
        flash("Unable to remove admin.", "danger")

    return redirect(url_for("admin.admin_management"))