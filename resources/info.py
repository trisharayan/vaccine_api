import sqlite3
from flask_restful import Resource
from flask import request

class infoClass(Resource):
    def post(self):
        data = request.get_json()
        if(data['action']=="getname"):
            with sqlite3.connect("Database.db") as con:
                crsr = con.cursor()
                crsr.execute("select user_name,dob from user_profile_table where email_id = ?",(data['email_id'],))
                rows = crsr.fetchall()
                con.commit()
                return rows


