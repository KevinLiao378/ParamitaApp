#!/usr/bin/python
#coding=utf-8

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import config
import datetime

app = Flask(__name__)
app.config.from_object(config['development'])
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True)
    createdAt = db.Column(db.String(64))

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.createdAt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return '<User %r>' % self.username

    def to_json(self):
        json_user = {
            'id': self.id,
            'username': self.username,
            'createdAt': self.createdAt
        }
        return json_user


@app.route('/api/v1/users/<int:id>', methods = ['GET'])
def get_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'code': 0, 'message': '用户不存在'})
    return jsonify({
        'code': 1, 
        'message': 'success', 
        'data': user.to_json()
        })


@app.route('/api/v1/users', methods = ['GET'])
def get_all_users():
    users = User.query.all();
    json_users = []
    for user in users:
        json_users.append(user.to_json())
    return jsonify({
        'code': 1,
        'message': 'success',
        'data': json_users
        })


@app.route('/api/v1/users', methods = ['POST'])
def create_user():
    pass
    if not request.json:
        return jsonify({'code': 0, 'message': '错误的数据格式'})
    requestJson = request.get_json()
    username = requestJson['username']
    password = requestJson['password']
    queryResult = User.query.filter_by(username=username).first()
    if queryResult is None:
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        return jsonify({'code': 1, 'message': 'success'})
    return jsonify({'code': 0, 'message': '用户已存在'})


@app.route('/api/v1/users/<int:id>', methods = ['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({'code': 0, 'message': '用户不存在'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'code': 1, 'message': 'success'})


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    app.run(debug=True)