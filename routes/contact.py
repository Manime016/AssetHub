from flask import Blueprint, request, redirect, url_for, flash, render_template

from database.connection import get_db_connection
from database.contact_queries import ContactQueries

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact")
def contact():

    return render_template("contact.html")


@contact_bp.route("/contact_submit", methods=["POST"])
def contact_submit():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    db = get_db_connection()

    contact_queries = ContactQueries(db)

    if contact_queries.add_message(name, email, message):

        flash("Message sent successfully.", "success")

    else:

        flash("Unable to send message.", "danger")

    return redirect(url_for("contact.contact"))