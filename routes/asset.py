from flask import Blueprint, request, redirect, url_for, flash, render_template
from database.connection import get_db_connection
from database.asset_queries import AssetQueries

asset_bp = Blueprint("asset", __name__)


@asset_bp.route("/asset_info")
def asset_info():
    db_connection = get_db_connection()
    asset_queries = AssetQueries(db_connection)

    assigned_assets = asset_queries.asset_info() or []
    all_assets = asset_queries.all_assets() or []

    return render_template(
        "index.html",
        assigned_assets=assigned_assets,
        all_assets=all_assets
    )


@asset_bp.route("/filter_info")
def filter_info():
    search_by = request.args.get("search_type")
    search_value = request.args.get("search_value")

    db_connection = get_db_connection()
    asset_queries = AssetQueries(db_connection)

    if search_by == "emp":
        column = "employee_id"
    elif search_by == "asset":
        column = "asset_id"
    else:
        column = None

    if column and search_value:
        assigned_assets = asset_queries.filter_info(column, search_value) or []
    else:
        assigned_assets = asset_queries.asset_info() or []

    all_assets = asset_queries.all_assets() or []

    return render_template(
        "index.html",
        assigned_assets=assigned_assets,
        all_assets=all_assets
    )


@asset_bp.route("/all_assets")
def all_assets():
    db_connection = get_db_connection()
    asset_queries = AssetQueries(db_connection)

    assigned_assets = asset_queries.asset_info() or []

    category = request.args.get("search_category")

    if category:
        inventory = asset_queries.filter_category(category) or []
    else:
        inventory = asset_queries.all_assets() or []

    return render_template(
        "index.html",
        assigned_assets=assigned_assets,
        all_assets=inventory
    )


@asset_bp.route("/assign_asset/<asset_id>", methods=["POST"])
def assign_asset(asset_id):
    employee_id = request.form.get("employee_id")

    if not employee_id:
        flash("Employee ID is required.", "danger")
        return redirect(url_for("asset.asset_info"))

    db_connection = get_db_connection()
    asset_queries = AssetQueries(db_connection)

    # Requires assign_asset() method in AssetQueries
    asset_queries.assign_asset(asset_id, employee_id)

    flash("Asset assigned successfully.", "success")
    return redirect(url_for("asset.asset_info"))

@asset_bp.route("/return_asset/<asset_id>", methods=["POST"])
def return_asset(asset_id):
    db = get_db_connection()
    asset_queries = AssetQueries(db)

    if asset_queries.return_asset(asset_id):
        flash("Asset returned successfully.", "success")
    else:
        flash("Unable to return asset.", "danger")

    return redirect(url_for("asset.asset_info"))

@asset_bp.route("/add_asset")
def add_asset_page():
    return render_template("add_asset.html")


@asset_bp.route("/add_asset", methods=["POST"])
def add_asset():

    asset_id = request.form.get("asset_id")
    asset_name = request.form.get("asset_name")
    category = request.form.get("category")
    purchase_date = request.form.get("purchase_date")
    purchase_price = request.form.get("purchase_price")

    db = get_db_connection()
    asset_queries = AssetQueries(db)

    success = asset_queries.add_asset(
        asset_id,
        asset_name,
        category,
        purchase_date,
        purchase_price
    )

    if success:
        flash("Asset added successfully.", "success")
    else:
        flash("Unable to add asset.", "danger")

    return redirect(url_for("asset.add_asset_page"))


