# database/login_queries.py

class LoginQueries:
    def __init__(self, connection):
        self.connection = connection

    def get_employee_by_id(self, employee_id):
        if not self.connection:
            print("❌ No database connection. Cannot fetch employee.")
            return None

        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM admin WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print(f"❌ Error fetching employee: {e}")
            return None

    def verify_employee(self, employee_id, password):
        employee = self.get_employee_by_id(employee_id)
        if employee:
            # Assuming password is at index 2 of your DB schema; adjust as necessary
            # Ideally, use a password hashing check here like werkzeug.security.check_password_hash
            db_password = employee[2] 
            return db_password == password
        return False