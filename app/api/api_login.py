from flask import request, session, render_template, redirect, url_for
from app.services.srv_user import UserService
from app.api import routes
from app.schemas.sche_base import Message

@routes.route('/login', methods=['GET'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    account = UserService.authentication(username=username, password=password)
    msg: str
    stt: bool
    if account:
        session['loggedin'] = True
        session['id'] = account['id']
        session['username'] = account['username']
        msg = 'Logged in successfully!'
        stt = True
    else:
        msg = 'Incorrect username/ password'
        stt = False
    return Message(
        status=stt,
        message=msg
    ).dict()
