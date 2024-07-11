# add labtest
import pymysql
from flask import *
import pymysql.cursors
from functions import *
from flask_restful import Resource
class AddLabTest(Resource):
    def post(self):
        data = request.json
        test_name = data["test_name"]
        test_description = data["test_description"]
        test_cost = data["test_cost"]
        test_discount = data["test_discount"]

        connection = pymysql.connect(host = 'localhost',  user ='root', password='', database ='bliss')
        cursor = connection.cursor()

        sql = "insert into lab_tests (test_name, test_description, test_cost,test_discount) values(%s,%s,%s,%s)"
        data =(test_name, test_description, test_cost,test_discount)
        cursor.execute(sql, data)
        connection.commit()

        return jsonify({"message" : " LabTest added succesfully"})
        

