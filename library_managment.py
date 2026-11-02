import mysql.connector
import datetime


class get_connection:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Saneem@1212",
                database="book_db"

            )
            return self.connection
        except Exception as e:
            return None

class books(get_connection):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from book_details"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            # print(record)
            return record
        except Exception as e:
            print()

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query ="insert into book_details(book_name,author_name,price,type,published_year) values(%s, %s, %s, %s, %s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("new book added successfully..!")
        except Exception as e:
            print(e)
    # def post(self, **kwargs):
    #     try:
    #         self.connect = super().get_connection()
    #         self.cursor = self.connect.cursor()
    #         query = "insert into book_details(book_name,author_name,price,type,published_year) values(%s, %s, %s, %s, %s)"
    #         values = [v for v in kwargs.values()]
    #         self.cursor.execute(query, values)
    #         self.connect.commit()
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False