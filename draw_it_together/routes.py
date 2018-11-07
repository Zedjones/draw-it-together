from draw_it_together import app 
from flask import request
from flask import jsonify
import json
import db_ops

@app.route('/')
@app.route('/index')
def index():
    test = db_ops.connect()
    return str(type(test))

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.headers['Content-Type'] == 'application/json':
        if not ('name' in request.json and 'id' in request.json):
            return "Name and ID are required."
        name = request.json['name']
        user_id = request.json['id']
        db_ops.db_add_user(user_id, name)
        return "Successfully added user to the DB."
    return "JSON body is required."

@app.route('/clear_users', methods=['POST'])
def clear_users():
    db_ops.db_clear_table('users')
    return "Table users successfully cleared."

@app.route('/clear_pictures', methods=['POST'])
def clear_pictures():
    db_ops.db_clear_table('pictures')
    return "Table pictures successfully cleared."

@app.route('/check_user', methods=['POST'])
def check_user():
    if request.headers['Content-Type'] == 'application/json':
        if not 'name' in request.json:
            return "Name is required."
        name = request.json['name']
        return jsonify(
            exists=db_ops.db_check_for_name(name)
        )
    else:
        return "JSON body is required."

@app.route('/add_picture', methods=['POST'])
def add_picture():
    if request.headers['Content-Type'] == 'application/json':
        if not ('name' in request.json and 'picture' in request.json):
            return "Name and picture are required"
        name = request.json['name']
        img_base_64 = request.json['picture']
        db_ops.db_add_image(name, img_base_64)
    return "Good"