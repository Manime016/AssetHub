class EmployeeQueries:
    def __init__(self, connection):
        self.connection = connection

    def add_employee(self, employee_id, employee_name, employee_email, department, phone, designation):
        if not self.connection:
            print("❌ No database connection. Cannot add employee.")
            return False

        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO Employee (employee_id, name, email, department, phone, designation) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (employee_id, employee_name, employee_email, department, phone, designation))
            self.connection.commit() 
            cursor.close()
            return True
        except Exception as e:
            print(f"❌ Error adding employee: {e}")
            if self.connection:
                self.connection.rollback()
            return False
    
    def search_employee(self, search_by, search_query):
        if not self.connection:
            print("❌ No database connection. Cannot search employee.")
            return []

        try:
            cursor = self.connection.cursor(dictionary=True)
            if search_by == "name":
                query = "SELECT * FROM Employee WHERE name LIKE %s"
                cursor.execute(query, (f"%{search_query}%",))
            elif search_by == "employee_id":
                query = "SELECT * FROM Employee WHERE employee_id = %s"
                cursor.execute(query, (search_query,))
            else:
                cursor.close()
                return []

            result = cursor.fetchall()
            cursor.close()
            return result if result is not None else []
            
        except Exception as e:
            print(f"❌ Error searching for employee: {e}")
            return []
        
    def delete_employee(self, employee_id):
        if not self.connection:
            print("❌ No database connection. Cannot delete employee.")
            return False

        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM Employee WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            self.connection.commit() 
            cursor.close()
            return True
        except Exception as e:
            print(f"❌ Error deleting employee: {e}")
            if self.connection:
                self.connection.rollback()
            return False    
        
    # FIX: Re-engineered to process updates dynamically based on altered values
    def edit_employee(self, employee_id, updates):
        if not self.connection:
            print("❌ No database connection. Cannot edit employee.")
            return False

        try:
            cursor = self.connection.cursor()
            
            # Formulate the SET structure cleanly (e.g., "name = %s, department = %s")
            set_clause = ", ".join([f"{column} = %s" for column in updates.keys()])
            
            query = f"""
                UPDATE Employee 
                SET {set_clause} 
                WHERE employee_id = %s
            """
            
            # Safely arrange argument array (values to inject followed by row ID criteria)
            query_values = list(updates.values()) + [employee_id]
            
            cursor.execute(query, query_values)
            self.connection.commit() 
            cursor.close()
            return True
        except Exception as e:
            print(f"❌ Error editing employee: {e}")
            if self.connection:
                self.connection.rollback()
            return False