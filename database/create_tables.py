from database.connection import get_db_connection  # Import DB connection function

class create_tables:
    def __init__(self):
        self.connection = get_db_connection()
        if self.connection:
            print("✅ Database connection established.")
        else:
            print("❌ Failed to establish database connection.")

    def create_tables(self):
        if not self.connection:
            print("❌ No database connection. Cannot create tables.")
            return

        try:
            cursor = self.connection.cursor()

            # 1. Create Employee table cleanly with full attributes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Employee (
                    employee_id VARCHAR(20) PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    department VARCHAR(50),
                    password VARCHAR(255) NOT NULL,  -- Store hashed passwords
                    phone VARCHAR(15),
                    designation VARCHAR(50),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                );
            """)
            print("✅ 'Employee' table verified (created if missing).")

            # 2. Create Asset table cleanly with Foreign Key referencing Employee
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Asset (
                    asset_id VARCHAR(50) PRIMARY KEY,   
                    asset_name VARCHAR(100) NOT NULL,
                    category VARCHAR(50), 
                    purchase_date DATE,
                    purchase_price DECIMAL(10, 2),
                    status VARCHAR(20) DEFAULT 'Available',
                    employee_id VARCHAR(20),    
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id) ON DELETE SET NULL
                );
            """)
            print("✅ 'Asset' table verified (created if missing).")
            
            self.connection.commit()
            
        except Exception as e:
            print(f"❌ Error creating tables: {e}")
        finally:
            cursor.close()
            # It's a good practice to close the connection if this is a one-time script
            self.connection.close() 

if __name__ == "__main__":
    db_creator = create_tables()
    db_creator.create_tables()