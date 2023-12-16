from dotenv import load_dotenv
from flask import Flask, current_app
from flask_cors import CORS
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from fuzzywuzzy import fuzz
import hashlib
import jwt
import logging
from flask import Flask, jsonify, request, current_app
from time import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import *
from flask_httpauth import HTTPTokenAuth

load_dotenv()

db_username = 'benson'
db_password = 'Abc123456789!'
db_host = '34.80.114.185'
db_port = '3306'
db_name = 'project'


app = Flask(__name__)
CORS(app, resources={r"/*": {'origins': "*"}})
app.config['SECRET_KEY'] = 'secret'

#連線到伺服器上的 MySQL
db_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(db_url, echo=True)
Session=sessionmaker(bind=engine)
session=Session()

# Flask authentication configs
app.config.from_object(__name__)

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return ("Hello, world!")


@app.route('/bricks', methods=['GET'])
def bricks():
    return ("他媽的商務應用 操!")


@app.route('/bricks_login', methods=['POST'])
def bricks_login():
    response_object = {'status': 'success'}
    response_object['message'] = "登入成功"
    post_data = request.get_json()
    try:
        user=session.query(User).filter(User.user_email==post_data.get('user_email')).first()
        response_object['user_id'] = user.id
        user_password = user.user_password
        if user_password != post_data.get("username"):
            response_object['status'] = "failure"
            response_object['message'] = "您的密碼不正確，請再試一次"
            return jsonify(response_object)
    except IndexError:
        response_object['status'] = "failure"
        response_object['message'] = "您的帳號不正確，請再試一次"
        return jsonify(response_object)
    except:
        response_object['status'] = "failure"
        response_object['message'] = "SELECT user_id 失敗"
        return jsonify(response_object)

    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
