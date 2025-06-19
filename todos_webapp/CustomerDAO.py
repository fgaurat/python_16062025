import sqlite3
from Customer import Customer
from typing import Generator

class CustomerDAO:

    def __init__(self,db_file):
        self.__con = sqlite3.connect(db_file)
    
    def findAll(self):
        cur = self.__con.cursor()
        sql = "SELECT id,first_name,last_name,email,gender,ip_address FROM customers"
        res = cur.execute(sql)
        for data in res.fetchall():
            c = Customer(*data)
            yield c

    def __del__(self):
        self.__con.close()
