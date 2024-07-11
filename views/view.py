import pymysql
from flask import *
import pymysql.cursors
from functions import *
from flask_restful import Resource
# add a member class
# member sign up
class membersignup(Resource):
    def post(self):
        # get data from client
        data = request.json
        surname = data["surname"]
        middle_name =data["middle_name"]
        others = data["others"]
        gender = data["gender"]
        email = data["email"]
        phone = data["phone"]
        date_of_birth =data["date_of_birth"]
        password = data["password"]
        location_id = data["location_id"]

        # check if password is valid
        response = check_password(password)
        if response == True:
            # connect to DB
            connection = pymysql.connect(host = 'localhost',  user ='root', password='', database ='bliss')
            cursor = connection.cursor()
            # insert into database
            sql = "insert into members (surname, middle_name, others, gender, email, phone, date_of_birth, password, location_id) values(%s,%s,%s,%s,%s, %s,%s,%s,%s)"
            data =(surname, middle_name, others, gender, email, phone, date_of_birth, hash_password(password), location_id)
            cursor.execute(sql, data)
            connection.commit()
            return jsonify({"message" : " member saved succesfully"})
        else:
            return jsonify({ "message" : response})

# member signin
class membersignin(Resource):
    def post(self):
        data = request.json
        email = data["email"]
        password =data["password"]

        # connection to DB

        connection = pymysql.connect(host = 'localhost',  user ='root', password='', database ='bliss')
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # sql to check email if it exists

        sql = "select * from members where email = %s"
        # execute 
        cursor.execute(sql, email)
        # check for row count if it is 0 it means email dont exist
        if cursor.rowcount == 0:
            return jsonify({ "message" : "Email doesnt exist" })
        else:
            # return jsonify({ "message" : "Email exists" })
            # fetch member
            member= cursor.fetchone()
            hashed_password = member['password']
            is_matchpassword = hash_verify(password, hashed_password )
            # is_matchpassword can either be true or false
            if is_matchpassword == True:
                return jsonify({"member" : member })
            elif is_matchpassword == False:
                return jsonify({"message" : "LOGIN FAILED"})
            else:
                return jsonify({ "message": "Something went wrong" })
            
# memeber profile
class MemberProfile(Resource):
    def post(self):
        data = request.json
        member_id = data['member_id']
        # connect to DB
        connection = pymysql.connect(host = 'localhost',  user ='root', password='', database ='bliss')
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        sql = "select * from members where member_id = %s"
        # execute
        cursor.execute(sql, member_id)

        # check for row count
        member = cursor.fetchone()
        if cursor.rowcount == 0:
            
            return jsonify({ "message" : "Member doesnt exist" })
        else:
            return jsonify({"message": member})
        
        # make booking
class makebooking(Resource):
    def post(self):
        data = request.json
        member_id = data["member_id"]
        test_id = data["test_id"]
        appointment_date = data["appointment_date"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        status = data["status"]
        invoice_number = data["invoice_number"]

        # connect to DB
        connection = pymysql.connect(host = 'localhost',  user ='root', password='', database ='bliss')
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # insert into database
        sql = "insert into booking(member_id, test_id, appointment_date, latitude, longitude, status, invoice_number) values(%s,%s,%s,%s,%s, %s,%s)"
        data = (member_id, test_id, appointment_date, latitude, longitude, status, invoice_number)
        cursor.execute(sql, data)
        connection.commit()

        return jsonify({ "message": "POST SUCCESSFUL. BOOKING COMPLETED"})
    

    
