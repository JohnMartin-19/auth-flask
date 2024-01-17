from flask import Flask,Resource,request,response,jsonify,session

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

if __name__ == '__main__':
    app.run(debug=True)
