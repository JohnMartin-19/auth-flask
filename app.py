from flask import Flask,Resource,request,response,jsonify,session,api
from models import User
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'

class Login(Resource):

    def post(self):
        user = User.query.filter(
            User.username == request.get_json()['username']
        ).first()

        session['user_id'] = user.id
        return jsonify(user.to_dict())
api.add_resource(Login,'/login')

class CheckSession(Resource):

    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return jsonify(user.to_dict())
        else:
            return jsonify({'message': '401: Not Authorized'}), 401

api.add_resource(CheckSession, '/check_session')

class Logout(Resource):
    def get():
     session['user_id'] = None
     return jsonify({'message': '204: No Content'}), 204

api.add_resource(Logout, '/logout')



if __name__ == '__main__':
    app.run(debug=True)
