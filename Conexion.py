import sys, psycopg2

import data as data
import self as self
from psycopg2 import sql


class Conecttion():
    def __init__(self):
             self.conn = psycopg2.connect(
             database="persona",
             user="postgres",
             password="sapito19",
             host="localhost",
             port="5432",
            )
    conn = None
    cursor = None


    def execute(self, sql, data):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql, data)
            self.conn.commit()
            self.conn.rollback()

        except (Exception, psycopg2.DatabaseError) as ex:
            print(ex)
        finally:
            self.cursor.close()

    def executeQuery(self, sql,data):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql, id)
            data
            self.cursor.fetchall()
        finally:
            self.cursor.close
