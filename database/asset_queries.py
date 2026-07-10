# asset_queries.py

from mysql.connector import Error


class AssetQueries:

    def __init__(self, connection):
        self.connection = connection

    # ----------------------------
    # Assigned Assets
    # ----------------------------
    def asset_info(self):
        try:
            cursor = self.connection.cursor(dictionary=True)

            query = """
                SELECT *
                FROM asset
                WHERE employee_id IS NOT NULL
                ORDER BY asset_id
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Error as e:
            print("Database Error:", e)
            return []

        finally:
            cursor.close()

    # ----------------------------
    # All Assets
    # ----------------------------
    def all_assets(self):
        try:
            cursor = self.connection.cursor(dictionary=True)

            query = """
                SELECT *
                FROM asset
                ORDER BY asset_id
            """

            cursor.execute(query)
            return cursor.fetchall()

        except Error as e:
            print("Database Error:", e)
            return []

        finally:
            cursor.close()

    # ----------------------------
    # Filter Assigned Assets
    # ----------------------------
    def filter_info(self, column, value):
        try:
            cursor = self.connection.cursor(dictionary=True)

            if column not in ["employee_id", "asset_id"]:
                return []

            query = f"""
                SELECT *
                FROM asset
                WHERE {column} = %s
            """

            cursor.execute(query, (value,))
            return cursor.fetchall()

        except Error as e:
            print("Database Error:", e)
            return []

        finally:
            cursor.close()

    # ----------------------------
    # Filter Inventory by Category
    # ----------------------------
    def filter_category(self, category):
        try:
            cursor = self.connection.cursor(dictionary=True)

            query = """
                SELECT *
                FROM asset
                WHERE category LIKE %s
                ORDER BY asset_id
            """

            cursor.execute(query, ("%" + category + "%",))
            return cursor.fetchall()

        except Error as e:
            print("Database Error:", e)
            return []

        finally:
            cursor.close()

    # ----------------------------
    # Assign Asset
    # ----------------------------
    def assign_asset(self, asset_id, employee_id):
        try:
            cursor = self.connection.cursor()

            query = """
                UPDATE asset
                SET employee_id = %s,
                    status = 'Assigned'
                WHERE asset_id = %s
            """

            cursor.execute(query, (employee_id, asset_id))
            self.connection.commit()

            return cursor.rowcount > 0

        except Error as e:
            print("Database Error:", e)
            self.connection.rollback()
            return False

        finally:
            cursor.close()

    # ----------------------------
    # Return Asset
    # ----------------------------
    def return_asset(self, asset_id):
        try:
            cursor = self.connection.cursor()

            query = """
                UPDATE asset
                SET employee_id = NULL,
                    status = 'Available'
                WHERE asset_id = %s
            """

            cursor.execute(query, (asset_id,))
            self.connection.commit()

            return cursor.rowcount > 0

        except Error as e:
            print("Database Error:", e)
            self.connection.rollback()
            return False

        finally:
            cursor.close()

    # ----------------------------
    # Add Asset
    # ----------------------------
    def add_asset(
        self,
        asset_id,
        asset_name,
        category,
        purchase_date,
        purchase_price
    ):
        try:
            cursor = self.connection.cursor()

            query = """
                INSERT INTO asset
                (
                    asset_id,
                    asset_name,
                    category,
                    purchase_date,
                    purchase_price,
                    status
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    'Available'
                )
            """

            cursor.execute(
                query,
                (
                    asset_id,
                    asset_name,
                    category,
                    purchase_date,
                    purchase_price
                )
            )

            self.connection.commit()
            return True

        except Error as e:
            print("Database Error:", e)
            self.connection.rollback()
            return False

        finally:
            cursor.close()