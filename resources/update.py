from flask_restful import Resource,request
import sqlite3
import time
import datetime
from resources.login import login

sql_command = """CREATE TABLE IF NOT EXISTS vaccine_record_table (record_id INTEGER PRIMARY KEY,email_id VARCHAR(100),
vaccine_name VARCHAR(10),hospital VARCHAR(100), vaccine_taken_date VARCHAR(10), comment VARCHAR(400), created_date VARCHAR(10));"""

with sqlite3.connect("Database.db") as con:
    crsr = con.cursor()
    crsr.execute(sql_command)
    con.commit()


def insert_record(email_id,vaccine_name,hospital,vaccine_taken_date,comment):
    currentDT = datetime.datetime.now()
    date = currentDT.strftime("%d/%m/%Y")
    print(email_id)
    try:
        with sqlite3.connect("Database.db") as con:
            crsr = con.cursor()
            crsr.execute(
                "INSERT INTO vaccine_record_table(email_id,vaccine_name,hospital,vaccine_taken_date,comment,created_date) VALUES (?,?,?,?,?,?)",
                (email_id, vaccine_name, hospital, vaccine_taken_date, comment, date))
            con.commit()
        return True
    except:
        return False

def getRecord(email_id):
        with sqlite3.connect("Database.db") as con:
            crsr = con.cursor()
            crsr.execute("SELECT * FROM vaccine_record_table WHERE email_id=?", (email_id,))
            rows = crsr.fetchall()
            con.commit()
        return rows

class update(Resource):
    def post(self):
        data = request.get_json()
        if(login(data["email_id"],data["password"])):
            if(data["action"]=="insert"):
                return insert_record(data["email_id"],data["vaccine_name"],data["hospital"],data["vaccine_taken_date"],data["comment"])
            elif (data["action"] == "getrecord"):
                return getRecord(data["email_id"])

        return False



class delete(Resource):
    def post(self):
        data = request.get_json()
        if(login(data["email_id"],data["password"])):
            if(data["action"]=="delete"):
                return delete_record(data["email_id"],data["vaccine_name"],data["hospital"],data["vaccine_taken_date"],data["comment"])

        return False


def delete_record(email_id,vaccine_name,hospital,vaccine_taken_date,comment):
    with sqlite3.connect("Database.db") as con:
        crsr = con.cursor()
        crsr.execute("DELETE FROM vaccine_record_table WHERE email_id=? AND vaccine_name=? AND hospital= ? AND vaccine_taken_date= ? AND comment=?", (email_id,vaccine_name,hospital,vaccine_taken_date,comment,))
        con.commit()
    return True