from mysql.connector import Error


class ContactQueries:

    def __init__(self, connection):
        self.connection = connection

    def add_message(self, name, email, message):

        try:

            cursor = self.connection.cursor()

            query = """
            INSERT INTO contact_messages
            (
                name,
                email,
                message
            )
            VALUES
            (
                %s,
                %s,
                %s
            )
            """

            cursor.execute(query, (name, email, message))

            self.connection.commit()

            return True

        except Error as e:

            print(e)

            self.connection.rollback()

            return False

        finally:

            cursor.close()


    def get_messages(self):

        try:

            cursor = self.connection.cursor(dictionary=True)

            query = """
            SELECT *
            FROM contact_messages
            ORDER BY submitted_at DESC
            """

            cursor.execute(query)

            return cursor.fetchall()

        except Error as e:

            print(e)

            return []

        finally:

            cursor.close()