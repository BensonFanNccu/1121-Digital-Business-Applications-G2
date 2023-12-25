# from dotenv import load_dotenv
from flask import Flask, current_app
from flask_cors import CORS
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
# from fuzzywuzzy import fuzz
import hashlib
# import jwt
import logging
from flask import Flask, jsonify, request, current_app
from time import time
from sqlalchemy import create_engine, text
from sqlalchemy.orm import *
from flask_httpauth import HTTPTokenAuth

# load_dotenv()

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
def get_order():
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
def get_cancel_order():
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

@app.route('/get_retention_rate', methods=['POST'])
def get_retention_rate():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    post_data = request.get_json()
    year = post_data.get("year")
    period = post_data.get("period")

    try:
        if period == 1:
            query_curyr = f"""
                SELECT count(distinct(o.CustomerID)) FROM orders as o 
                WHERE (o.Date BETWEEN '{year}/1/1' AND '{year}/3/31') 
                AND o.CustomerID in (SELECT ol.CustomerID FROM orders ol WHERE ol.Date BETWEEN '{year - 1}/10/1' AND '{year - 1}/12/31');
            """

            query_lastyr = f"""
                SELECT count(distinct(o.CustomerId)) FROM orders o
                WHERE o.Date BETWEEN '{year - 1}/10/1' AND '{year - 1}/12/31';
            """
        
        elif period == 2:
            query_curyr = f"""
                SELECT count(distinct(o.CustomerID)) FROM orders as o 
                WHERE (o.Date BETWEEN '{year}/4/1' AND '{year}/6/30') 
                AND o.CustomerID in (SELECT ol.CustomerID FROM orders ol WHERE ol.Date BETWEEN '{year}/1/1' AND '{year}/3/31');
            """
            query_lastyr = f"""
                SELECT count(distinct(o.CustomerId)) FROM orders o
                WHERE o.Date BETWEEN '{year}/1/1' AND '{year}/3/31';
            """

        elif period == 3:
            query_curyr = f"""
                SELECT count(distinct(o.CustomerID)) FROM orders as o 
                WHERE (o.Date BETWEEN '{year}/7/1' AND '{year}/9/30') 
                AND o.CustomerID in (SELECT ol.CustomerID FROM orders ol WHERE ol.Date BETWEEN '{year}/4/1' AND '{year}/6/30');
            """
            query_lastyr = f"""
                SELECT count(distinct(o.CustomerId)) FROM orders o
                WHERE o.Date BETWEEN '{year}/4/1' AND '{year}/6/30';
            """

        else:
            query_curyr = f"""
                SELECT count(distinct(o.CustomerID)) FROM orders as o 
                WHERE (o.Date BETWEEN '{year}/10/1' AND '{year}/12/31') 
                AND o.CustomerID in (SELECT ol.CustomerID FROM orders ol WHERE ol.Date BETWEEN '{year}/7/1' AND '{year}/9/30');
            """
            query_lastyr = f"""
                SELECT count(distinct(o.CustomerId)) FROM orders o
                WHERE o.Date BETWEEN '{year}/7/1' AND '{year}/9/30';
            """

        result_cur = conn.execute(text(query_curyr))
        row_cur = result_cur.fetchone()
        count_cur = row_cur[0]

        result_last = conn.execute(text(query_lastyr))
        row_last = result_last.fetchone()
        count_last = row_last[0]

        
        if count_last == 0:
            retRate = '--'
            dictRR = {"retention rate: " : retRate}
            response_object['value'] = dictRR
        else:
            retRate = count_cur / count_last
            dictRR = {"retention rate: " : str(retRate)}
            response_object['value'] = dictRR

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)

    response_object['message'] = f"成功搜尋{year}年第{period}期的留存率資料"
    result_cur.close()
    result_last.close()
    conn.close()
    
    return jsonify(response_object)

@app.route('/get_survival_rate', methods=['POST'])
def get_survival_rate():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    post_data = request.get_json()
    year = post_data.get("year")
    period = post_data.get("period")

    surRate = 1

    try:
        for i in range(1, period + 1):
            if i == 1:
                query_curyr = f"""
                    SELECT count(distinct(o.CustomerID)) FROM orders as o 
                    WHERE (o.Date BETWEEN '{year}/1/1' AND '{year}/3/31') 
                    AND o.CustomerID in (SELECT ol.CustomerID FROM orders ol WHERE ol.Date BETWEEN '{year - 1}/10/1' AND '{year - 1}/12/31');
                """

                query_lastyr = f"""
                    SELECT count(distinct(o.CustomerId)) FROM orders o
                    WHERE o.Date BETWEEN '{year - 1}/10/1' AND '{year - 1}/12/31';
                """
            else:
                query_curyr = f"""
                    SELECT count(distinct(o.CustomerID)) FROM orders as o 
                    WHERE (o.Date BETWEEN '{year}/{i * 3 - 2}/1' AND '{year}/{i * 3}/31') 
                    AND o.CustomerID in (SELECT ol.CustomerID FROM orders ol WHERE ol.Date BETWEEN '{year}/{i * 3 - 5}/1' AND '{year}/{i * 3 - 3}/31');
                """

                query_lastyr = f"""
                    SELECT count(distinct(o.CustomerId)) FROM orders o
                    WHERE o.Date BETWEEN '{year}/{i * 3 - 5}/1' AND '{year}/{i * 3 - 3}/31';
                """

            result_cur = conn.execute(text(query_curyr))
            row_cur = result_cur.fetchone()
            count_cur = row_cur[0]

            result_last = conn.execute(text(query_lastyr))
            row_last = result_last.fetchone()
            count_last = row_last[0]

            if count_last == 0:
                surRate = 0
                dictSR = {"survival rate: " : surRate}
                response_object['value'] = dictSR
                break
            else:
                retRate = count_cur / count_last
                surRate *= retRate

            dictSR = {"survival rate: " : str(surRate)}
            response_object['value'] = dictSR

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)

    response_object['message'] = f"成功搜尋{year}年第{period}期的存活率資料"
    result_cur.close()
    result_last.close()
    conn.close()
    
    return jsonify(response_object)

@app.route('/LTV', methods=['POST'])
def LTV():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    post_data = request.get_json()
    id = post_data.get("CustomerID")

    current_time = datetime.now()
    current_month = current_time.month

    if current_month <= 3:
        quarter = 1
    elif current_month <=6:
        quarter = 2
    elif current_month <= 9:
        quarter = 3
    else:
        quarter = 4

    try:
        query = f"""
            SELECT sum(t.Price) FROM orders as o, ticketprice as t 
            WHERE o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID 
            AND o.CustomerID = {id} AND (o.Date BETWEEN '2023/{quarter * 3 - 2}/1' AND '2023/{quarter * 3}/31');
        """

        result = conn.execute(text(query))
        row = result.fetchone()
        value = row[0]
        
        LTV = value * (1 - 1 / (1.02) ** 4) / 0.02
        dictLTV = {"LTV: " : str(round(LTV, 4))}
        response_object['value'] = dictLTV

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"成功搜尋的顧客{id}的終身價值"
    result.close()
    conn.close()
    
    return jsonify(response_object)
    


if __name__ == "__main__":
    app.run(debug=True)
