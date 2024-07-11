from flask import *
from flask_restful import Resource, Api



app = Flask(__name__)
api = Api(app)

# import from views folder
from views.view import membersignup, membersignin, MemberProfile, makebooking



# add api endpoints or routes

api.add_resource(membersignup, '/api/member_signup')
api.add_resource(membersignin,'/api/member_signin')
api.add_resource(MemberProfile, '/api/member_profile')
api.add_resource(makebooking, '/api/makebooking') 
if __name__ == '__main__':
    app.run(debug=True)


