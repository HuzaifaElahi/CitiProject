from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
users = [
    {
        'username': 'dasdasdas',
        'password': 'd2321d2'
    }
]

@app.route('/')
def home():
    return render_template('index.html')


#@app.route('/') #:http://www.google.com/
#def home():
#    return "Hello, world!"

#POST - used to receive data
#GET - used to send data back only

#POST /user data: [name:]
@app.route('/user', methods=['POST'])
def create_user():
    request_data = request.get_json()
    new_user = {
        'username': request_data['username'],
        'password': request_data['password']
    }
    users.append(new_user)
    return jsonify(new_user)

#GET /user/<string:username>
@app.route('/user/<string:username>') #www.ggoogle.com/user/name
def get_user(username):
    #Iterate over users
    for user in users:
        if user['username'] == username:
            return jsonify(user)
    return jsonify({'message': 'users not found'})


#GET /user
@app.route('/user')
def get_users():
    return jsonify({'users': users})

#PUT 
@app.route('/user/<string:username>',  methods=['PUT'])
def update_password(username, newpassword):
    userthere = False
    for user in users:
        if user['username'] == username:
            userthere = True
            if user['password'] != newpassword:
                user['password'] = newpassword
    if(userthere == False):
        return jsonify({'message': 'users not found'})
    return jsonify({'message': 'you can not use the same password as before'})
        
    

#DELETE
@app.route('/user/<string:username>', methods=['DELETE'])
def delete_user(username):
    global users
    users = list(filter(lambda x: x['username'] != username, users))
    print (jsonify(users))
    return {'message': 'User deleted'}


#POST /store/<string:name>/item {name: price:}
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_in_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if store['name'] == name:
#             new_item = {
#                 'name': request_data['name'],
#                 'price': request_data['price']
#             }
#             store['items'].append(new_item)
#             return jsonify(new_item)
#     return jsonify({'message': 'store not found'})

# #GET /store/<string:name>/item
# @app.route('/store/<string:name>/item') #www.ggoogle.com/store/name
# def get_item_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return jsonify({'items': store['items']})
#     return jsonify({'message': 'store not found'})

app.run(port=5000)
