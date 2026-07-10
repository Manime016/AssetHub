from mysql.connector import Error


class AdminQueries:

    def __init__(self, connection):
        self.connection = connection

    # -------------------------
    # Get All Employees
    # -------------------------
    def get_all_employees(self):

        try:

            cursor = self.connection.cursor(dictionary=True)

            query = """
            SELECT
                e.employee_id,
                e.name,
                e.email,
                e.department,

                CASE
                    WHEN a.employee_id IS NULL THEN 0
                    ELSE 1
                END AS is_admin

            FROM employee e

            LEFT JOIN admin a
            ON e.employee_id = a.employee_id

            ORDER BY e.employee_id
            """

            cursor.execute(query)

            return cursor.fetchall()

        except Error as e:

            print(e)
            return []

        finally:

            cursor.close()

    # -------------------------
    # Promote Admin
    # -------------------------
    def promote_admin(self, employee_id, password):

        try:

            cursor = self.connection.cursor()

            cursor.execute(
                "SELECT employee_id FROM admin WHERE employee_id=%s",
                (employee_id,)
            )

            if cursor.fetchone():
                return False

            query = """
            INSERT INTO admin
            (
                employee_id,
                password
            )
            VALUES
            (
                %s,
                %s
            )
            """

            cursor.execute(query, (employee_id, password))

            self.connection.commit()

            return True

        except Error as e:

            print(e)

            self.connection.rollback()

            return False

        finally:

            cursor.close()

    # -------------------------
    # Remove Admin
    # -------------------------
    def remove_admin(self, employee_id):

        try:

            cursor = self.connection.cursor()

            query = """
            DELETE
            FROM admin
            WHERE employee_id=%s
            """

            cursor.execute(query, (employee_id,))

            self.connection.commit()

            return cursor.rowcount > 0

        except Error as e:

            print(e)

            self.connection.rollback()

            return False

        finally:

            cursor.close()