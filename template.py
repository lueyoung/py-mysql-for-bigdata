#!/usr/bin/env python
# -*- coding : UTF-8 -*-

import pymysql as pysql

def main():
    db = pysql.connect("192.168.31.241", "root", "123456", "BIGDATA")

    cursor = db.cursor()

    sql = "INSERT INTO EMPLOYEE (NAME, AGE, GENDER, INCOME) VALUES ('%s', '%s', '%s', '%s')" % ('Jone', 21, 'M', 2500)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    db.close()

if __name__ == "__main__":
    main()
