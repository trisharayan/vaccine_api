import sqlite3
import time
import datetime
from flask_restful import Resource
from flask import request


sql_command = """CREATE TABLE IF NOT EXISTS user_profile_table (user_id INTEGER PRIMARY KEY, email_id VARCHAR(100),password VARCHAR(100),user_name VARCHAR(100),
 national_id VARCHAR(100),address VARCHAR(500),gender VARCHAR(100),role VARCHAR(100),state VARCHAR(200),city VARCHAR(200),country VARCHAR(200),dob  VARCHAR(200),license_id VARCHAR(200),bussiness_national_id VARCHAR(200),hospitalName VARCHAR(200));"""

with sqlite3.connect("Database.db") as con:
    crsr = con.cursor()
    crsr.execute(sql_command)
    con.commit()




def register(user_name,email_id,password, national_id, address ,gender,role ,state,city,country,dob,license_id,bussiness_national_id,hospitalName):

   # try:
        with sqlite3.connect("Database.db") as con:
            crsr = con.cursor()
            crsr.execute("INSERT INTO user_profile_table (user_name,email_id,password, national_id, address ,gender,role ,state,city,country,dob,license_id,bussiness_national_id,hospitalName) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (user_name,email_id,password, national_id, address ,gender,role ,state,city,country,dob,license_id,bussiness_national_id,hospitalName))

            con.commit()
        return True
    #except:
    #   return False




def login(email_id,password):
    with sqlite3.connect("Database.db") as con:
        crsr = con.cursor()
        crsr.execute("select password from user_profile_table where email_id =?",(email_id,))
        rows=crsr.fetchall()
        con.commit()
        if(password==rows[0][0]):
            return True
        else:
            return False


#register("email_id","password", "user_name","SSN" ,"phone_no","gender" ,"s_que","s_ans")

#print(login("email_id","passord"))


class loginClass(Resource):
    def post(self):
        try:
            data = request.get_json()
            return login(data["email_id"],data["password"])
        except:
            return False

class registerClass(Resource):

    def post(self):
      #  try:
            data = request.get_json()
            return register(data["user_name"], data["email_id"],
                            data["password"], data["national_id"], data["address"],
                            data["gender"],data["role"], data["state"], data["city"], data["country"], data["dob"],data["license_id"],data["bussiness_national_id"],data["hospitalName"])
       # except:
        #    return False

