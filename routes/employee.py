from flask import Blueprint, request, redirect, url_for, flash, render_template
from database.connection import get_db_connection
from database.employee_queries import EmployeeQueries

employee_bp = Blueprint("employee", __name__)

def check_details(employee_name, employee_email, employee_id, department, phone, designation):
    if not employee_name or not employee_email or not employee_id or not department or not phone or not designation:
        flash("❌ All fields are required.", "danger")
        return False
    return True

@employee_bp.route("/add_employee-submit", methods=["POST"])
def add_employee_submit():
    employee_name = request.form.get("employee_name")
    employee_email = request.form.get("employee_email")
    employee_id = request.form.get("employee_id")
    department = request.form.get("department")
    phone = request.form.get("phone")
    designation = request.form.get("designation")

    if not check_details(employee_name, employee_email, employee_id, department, phone, designation):
        return redirect(url_for("pages.add_employee"))

    db_connection = get_db_connection() 
    employee_queries = EmployeeQueries(db_connection)

    if employee_queries.add_employee(employee_id, employee_name, employee_email, department, phone, designation):
        flash("✅ Employee added successfully!", "success")
        return redirect(url_for("pages.add_employee"))
    else:
        flash("❌ Error adding employee. Please try again.", "danger")
        return redirect(url_for("pages.add_employee"))
    
@employee_bp.route("/search")
def search_employee():
    search_by = request.args.get("search_by")
    search_query = request.args.get("search_query")
    
    employees = []
    
    # TO THIS:
    edit_id = request.args.get("edit_id")
    if (search_by and search_query) or edit_id:
        db_connection = get_db_connection()
        employee_queries = EmployeeQueries(db_connection)
        
# Pass "employee_id" and edit_id to your query if search_by is missing
        db_results = employee_queries.search_employee(search_by or "employee_id", search_query or edit_id)        
        if db_results is not None:
            employees = db_results
        else:
            employees = []
        
    return render_template("employee_list.html", employees=employees)

# Added proper route decorator matching your table link format
@employee_bp.route("/delete_employee/<employee_id>")
def delete_employee(employee_id):
    db_connection = get_db_connection()
    employee_queries = EmployeeQueries(db_connection)
    
    if employee_queries.delete_employee(employee_id):
        flash("✅ Employee deleted successfully!", "success")
    else:
        flash("❌ Error deleting employee. Please try again.", "danger")
    
    return redirect(url_for("pages.employee_list"))

# FIX: Added POST route decorator and implementation for tracking changes
@employee_bp.route("/edit_employee", methods=["POST"])
def edit_employee():
    employee_id = request.form.get("employee_id")
    if not employee_id:
        flash("❌ Missing Employee ID.", "danger")
        return redirect(url_for("pages.employee_list"))

    # Mapping out the input fields to evaluate changes
    fields = {
        "name": ("name", "orig_name"),
        "email": ("email", "orig_email"),
        "department": ("department", "orig_department"),
        "phone": ("phone", "orig_phone"),
        "designation": ("designation", "orig_designation")
    }

    updates = {}
    for db_column, (form_key, orig_key) in fields.items():
        new_val = request.form.get(form_key)
        orig_val = request.form.get(orig_key)
        
        # If the value changed, track it for our dynamic query execution
        if new_val != orig_val:
            updates[db_column] = new_val

    if not updates:
        flash("ℹ️ No modifications detected.", "info")
        return redirect(url_for("pages.employee_list"))

    db_connection = get_db_connection()
    employee_queries = EmployeeQueries(db_connection)
    
    # Hand the target updates payload to our custom dynamic query worker
    if employee_queries.edit_employee(employee_id, updates):
        flash("✅ Employee updated successfully!", "success")
    else:
        flash("❌ Error updating employee. Please try again.", "danger")
    
    return redirect(url_for("pages.employee_list"))