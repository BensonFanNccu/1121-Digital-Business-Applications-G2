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

# Flask authentication configs
app.config.from_object(__name__)

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return ("Hello, world!")


@app.route('/bricks', methods=['GET'])
def bricks():
    return ("他媽的商務應用 操!")


@app.route('/get_order', methods=['POST'])
def login():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    #取得資料
    post_data = request.get_json()
    flight_id = post_data.get("flight_id")
    date = post_data.get("date")
    #對比信箱，如正確回傳 user_id
    
    try:
        if (flight_id != None)&(date != None):

            query = f"""
                SELECT o.FlightID, o.CustomerId, o.PriceLevel, o.Date FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                WHERE f.FlightID = "{flight_id}"
                AND o.Date = "{date}"
                AND o.Status = "OK";
            """
        elif date != None:
            query = f"""
                SELECT o.FlightID, o.CustomerId, o.PriceLevel, o.Date FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                WHERE o.Date = "{date}"
                AND o.Status = "OK";
            """
        elif flight_id != None:
            query = f"""
                SELECT o.FlightID, o.CustomerId, o.PriceLevel, o.Date FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                WHERE f.FlightID = "{flight_id}"
                AND o.Status = "OK";
            """
        result = conn.execute(text(query))
        keys = list(result.keys())
        data = [dict(zip(keys, row)) for row in result.fetchall()]
        print(data)
        response_object['orders'] = data
            
    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"成功搜尋{flight_id}&{date}訂單資料"
    result.close()
    conn.close()
    
    return jsonify(response_object)

@app.route('/get_cancel_order', methods=['POST'])
def login():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    #取得資料
    post_data = request.get_json()
    flight_id = post_data.get("flight_id")
    date = post_data.get("date")
    #對比信箱，如正確回傳 user_id
    
    try:
        if (flight_id != None)&(date != None):

            query = f"""
                SELECT o.FlightID, o.CustomerId, o.PriceLevel, o.Date FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                WHERE f.FlightID = "{flight_id}"
                AND o.Date = "{date}"
                AND o.Status = "Cancel";
            """
        elif date != None:
            query = f"""
                SELECT o.FlightID, o.CustomerId, o.PriceLevel, o.Date FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                WHERE o.Date = "{date}"
                AND o.Status = "Cancel";
            """
        elif flight_id != None:
            query = f"""
                SELECT o.FlightID, o.CustomerId, o.PriceLevel, o.Date FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                WHERE f.FlightID = "{flight_id}"
                AND o.Status = "Cancel";
            """
        result = conn.execute(text(query))
        keys = list(result.keys())
        data = [dict(zip(keys, row)) for row in result.fetchall()]
        print(data)
        response_object['orders'] = data
            
    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"成功搜尋{flight_id}&{date}退單資料"
    result.close()
    conn.close()
    
    return jsonify(response_object)

if __name__ == "__main__":
    app.run(debug=True)
