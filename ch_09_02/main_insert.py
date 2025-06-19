import csv
import sqlite3


def main():

    with sqlite3.connect("customers.db") as con:
        cur = con.cursor()
        sql ="""INSERT INTO customers(first_name,last_name,email,gender,ip_address)
VALUES(?,?,?,?,?)
    """
        with open('MOCK_DATA.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile,delimiter=",")
            for data in reader:
                del data['id']
                cur.execute(sql,tuple(data.values()))


if __name__=='__main__':
    main()
