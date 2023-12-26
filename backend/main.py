# from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_httpauth import HTTPTokenAuth
from datetime import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine, text
from sqlalchemy.orm import *

import numpy as np
import pandas as pd

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
@app.route('/hello', methods=['GET'])
def greetings():
    return ("Hello, world!")


def query2dict(query, conn):
    result = conn.execute(text(query))
    keys = list(result.keys())
    data = [dict(zip(keys, row)) for row in result.fetchall()]
    return data

#模型相關
@app.route('/set_parameter', methods=['POST'])
def set_parameter():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    post_data = request.get_json()

    try:
        #寫入資料庫
        
        insert = f"""
            INSERT INTO modelparameter (Date, Demand, AbsentRate, FlightID)
            VALUES ('{post_data.get("date")}', {post_data.get("demand")}, {post_data.get("AbsentRate")}, {post_data.get("flight_id")}); 
        """
        conn.execute(text(insert))
        conn.execute(text("COMMIT;"))

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"參數設定成功"
    conn.close()
    
    return jsonify(response_object)


@app.route('/revenue_analysis', methods=['POST'])
def revenue_analysis():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    post_data = request.get_json()

    try:
        # for 迴圈計算多天收益之後加，先測試一天的
        #模型計算(把模型加在這裡)

        #測試資料
        date = None
        test_avaerge_daily_price = 0
        test_seat_level_num = [120, 150, 130]
        test_price_level = [7000, 6000, 4000]

        #模型輸出結果

        #預期收益
        avaerge_daily_price = test_avaerge_daily_price
        seat_level_num = test_seat_level_num
        price_level = test_price_level
        total_rev = 0
        for i in range(len(seat_level_num)):
            total_rev += seat_level_num[i]*price_level[i]
        response_object['predict_rev'] = total_rev
        
        #成長率
        last_year = 2022
        last_rev_query = f"""
            SELECT SUM(p.Price) AS last_year_rev FROM orders o
            JOIN ticketprice p
            ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
            WHERE o.Date BETWEEN '{last_year}/1/1' AND '{last_year}/12/31';
        """
        last_rev = query2dict(last_rev_query, conn)
        rev_grow_rate = (total_rev - last_rev[0]["last_year_rev"])/last_rev[0]["last_year_rev"]
        response_object['rev_grow_rate'] = rev_grow_rate

        #現有收益
        year = 2023
        q = [1, 4, 7, 10]
        rev_list = []
        for i in q:
            rev_query = f"""
                SELECT SUM(p.Price) AS rev FROM orders o
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                WHERE o.Date BETWEEN '{year}/{i}/1' AND '{year}/{i+2}/31';
            """
            rev = query2dict(rev_query, conn)
            rev_list.append(rev[0]["rev"])
        
        response_object['rev_every_q'] = rev_list

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = e
        print(e)
        return jsonify(response_object)
    
    response_object['message'] = f"參數設定成功"
    conn.close()
    
    return jsonify(response_object)


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


@app.route('/RFM', methods=['GET'])
def RFM():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    try:
        # RFM

        #設定分數
        def level(data, name):
            for i in range(len(data)):
                if i <= len(data) * 0.2:
                    data[i][name] = 5
                elif i <= len(data) * 0.4:
                    data[i][name] = 4
                elif i <= len(data) * 0.6:
                    data[i][name] = 3
                elif i <= len(data) * 0.8:
                    data[i][name] = 2
                elif i <= len(data):
                    data[i][name] = 1
            data = sorted(data, key = lambda x:x['CustomerID']) 
            return data
        
        #設定權重
        recency_weight = 0.3
        frequency_weight = 0.3
        monetary_weight = 0.4

        # Recency
        recency_query = f"""
            SELECT CustomerID, MAX(Date) AS recent_date FROM orders
            GROUP BY CustomerID
            ORDER BY recent_date;
        """
        recency_data = query2dict(recency_query, conn)
        recency_data = level(recency_data, "recency_level") 
        print(recency_data)

        #Frequency
        year = "2023"
        frequency_query = f"""
            SELECT CustomerID, COUNT(OrderID) AS frequency FROM orders
            WHERE Date BETWEEN '{year}/1/1' AND '{year}/12/31'
            GROUP BY CustomerID
            ORDER BY frequency DESC;
        """
        frequency_data = query2dict(frequency_query, conn)
        frequency_data = level(frequency_data, "frequency_level") 
        print(frequency_data)
        
        #Monetary
        monetary_query = f"""
            SELECT o.CustomerID, SUM(p.Price) AS monetary FROM orders o
            JOIN ticketprice p
            ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
            WHERE o.Date BETWEEN '{year}/1/1' AND '{year}/12/31'
            GROUP BY CustomerID
            ORDER BY monetary DESC;
        """
        monetary_data = query2dict(monetary_query, conn)
        monetary_data = level(monetary_data, "monetary_level") 
        print(monetary_data)

        #計算總分
        RFM_result = []
        for i in range(len(recency_data)):
            RFM_result.append(
            {
                "CustomerID": recency_data[i]["CustomerID"],
                "total_score": recency_data[i]["recency_level"]*recency_weight + frequency_data[i]["frequency_level"]*frequency_weight + monetary_data[i]["monetary_level"]*monetary_weight,
                "recency_score": recency_data[i]["recency_level"],
                "frequency_score": frequency_data[i]["frequency_level"],
                "monetary_score": monetary_data[i]["monetary_level"],
            })
        RFM_result = sorted(RFM_result, key = lambda x:x["total_score"], reverse=True)
        RFM_result = level(RFM_result, "RFM_group")
        RFM_result = sorted(RFM_result, key = lambda x:x["RFM_group"], reverse=True)
        print(RFM_result)
        response_object['RFM'] = RFM_result

        #寫入資料庫
        for i in RFM_result:
            update = f"""
                UPDATE customer SET RFM = {i["RFM_group"]} WHERE CustomerID = {i["CustomerID"]} 
            """
            conn.execute(text(update))
            conn.execute(text("COMMIT;"))
        

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    

    response_object['message'] = f""
    conn.close()
    
    return jsonify(response_object)


@app.route('/PCV', methods=['GET'])
def PCV():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    try:
        rate = 0.0125
        year = 2023
        query = f"""
            SELECT o.CustomerID, SUM(p.Price) AS PCV FROM orders o
            JOIN ticketprice p
            ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
            WHERE o.Date BETWEEN '{year}/1/1' AND '{year}/12/31'
            GROUP BY CustomerID
            ORDER BY PCV DESC;
        """
        past_value_data = query2dict(query, conn)
        for i in past_value_data:
            i["PCV"] = i["PCV"]/(1+rate)
        
        response_object['PCV'] = past_value_data

        #寫入資料庫
        for i in past_value_data:
            update = f"""
                UPDATE customer SET PCV = {i["PCV"]} WHERE CustomerID = {i["CustomerID"]} 
            """
            conn.execute(text(update))
            conn.execute(text("COMMIT;"))

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f""
    conn.close()
    
    return jsonify(response_object)


@app.route('/LTV', methods=['GET'])
def LTV():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

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
        queryCount = f"""
            SELECT count(CustomerID) AS count FROM customer;
        """
        countResult = conn.execute(text(queryCount))
        cRow = countResult.fetchone()
        custNum = cRow[0]

        year = 2023
        rate = 0.02
        LTVlist = []

        for i in range(1, custNum + 1):
            query = f"""
                SELECT sum(t.Price) FROM orders as o, ticketprice as t 
                WHERE o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID 
                AND o.CustomerID = {i} AND (o.Date BETWEEN '{year}/{quarter * 3 - 2}/1' AND '{year}/{quarter * 3}/31');
            """

            result = conn.execute(text(query))
            row = result.fetchone()
            value = row[0]

            if value != None:
                LTV = value * (1 - 1 / (1 + rate) ** 4) / rate
            else:
                LTV = 0

            dictLTV = {"CustomerID:" : i, "LTV" : str(round(LTV, 5))}
            LTVlist.append(dictLTV)
        
            update = f"""
                UPDATE customer SET LTV = {LTV} WHERE CustomerID = {i};
            """
            conn.execute(text(update))
            conn.execute(text("COMMIT;"))        
        
        response_object['LTV'] = LTVlist

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"成功搜尋的顧客的終身價值"
    result.close()
    countResult.close()
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
            RRlist = [dictRR]
            response_object['retention rate'] = RRlist
        else:
            retRate = count_cur / count_last
            dictRR = {"retention rate: " : retRate}
            RRlist = [dictRR]
            response_object['retention rate'] = RRlist

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


@app.route('/get_all_retention_rate', methods=['GET'])
def get_all_retention_rate():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    year = 2023
    RRlist = []

    try:
        for i in range(1, 5):
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
                    WHERE (o.Date BETWEEN '{year}/{i * 3 - 2}/1' AND '{year}/{i * 3}/30') 
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
                retRate = '--'
            else:
                retRate = count_cur / count_last
            
            dictRR = {"retention rate of quarter {}".format(str(i)) : retRate}
            RRlist.append(dictRR)

        response_object['retention rate'] = RRlist

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)

    response_object['message'] = f"成功搜尋{year}年的留存率資料"
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
                SRlist = [dictSR]
                response_object['survival rate'] = SRlist
                break
            else:
                retRate = count_cur / count_last
                surRate *= retRate
                dictSR = {"survival rate: " : surRate}
                SRlist = [dictSR]
                response_object['survival rate'] = SRlist

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

@app.route('/get_all_survival_rate', methods=['GET'])
def get_all_survival_rate():
    response_object = {'status': 'success'}
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    surRate = 1
    SRlist = []
    year = 2023

    try:
        for i in range(1, 5):
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
                    WHERE (o.Date BETWEEN '{year}/{i * 3 - 2}/1' AND '{year}/{i * 3}/30') 
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
            else:
                retRate = count_cur / count_last
                surRate *= retRate
            
            dictSR = {"survival rate of quarter {}".format(str(i)) : surRate}
            SRlist.append(dictSR)

        response_object['survival rate'] = SRlist
    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    response_object['message'] = f"成功搜尋{year}年的存活率資料"
    result_cur.close()
    result_last.close()
    conn.close()
    
    return jsonify(response_object) 
@app.route('/get_customer_info', methods=['GET'])
def get_customer_info():
    response_object = {'status': 'success'}

 
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    customer_info_list = []

    # RFM
    def get_RFM():
        try:
            #設定分數
            def level(data, name):
                for i in range(len(data)):
                    if i <= len(data) * 0.2:
                        data[i][name] = 5
                    elif i <= len(data) * 0.4:
                        data[i][name] = 4
                    elif i <= len(data) * 0.6:
                        data[i][name] = 3
                    elif i <= len(data) * 0.8:
                        data[i][name] = 2
                    elif i <= len(data):
                        data[i][name] = 1
                data = sorted(data, key = lambda x:x['CustomerID']) 
                return data
            
            #設定權重
            recency_weight = 0.3
            frequency_weight = 0.3
            monetary_weight = 0.4

            # Recency
            recency_query = f"""
                SELECT CustomerID, MAX(Date) AS recent_date FROM orders
                GROUP BY CustomerID
                ORDER BY recent_date;
            """
            recency_data = query2dict(recency_query, conn)
            recency_data = level(recency_data, "recency_level") 
            print(recency_data)

            #Frequency
            year = "2023"
            frequency_query = f"""
                SELECT CustomerID, COUNT(OrderID) AS frequency FROM orders
                WHERE Date BETWEEN '{year}/1/1' AND '{year}/12/31'
                GROUP BY CustomerID
                ORDER BY frequency DESC;
            """
            frequency_data = query2dict(frequency_query, conn)
            frequency_data = level(frequency_data, "frequency_level") 
            print(frequency_data)
            
            #Monetary
            monetary_query = f"""
                SELECT o.CustomerID, SUM(p.Price) AS monetary FROM orders o
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                WHERE o.Date BETWEEN '{year}/1/1' AND '{year}/12/31'
                GROUP BY CustomerID
                ORDER BY monetary DESC;
            """
            monetary_data = query2dict(monetary_query, conn)
            monetary_data = level(monetary_data, "monetary_level") 
            print(monetary_data)

            #計算總分
            RFM_result = []
            for i in range(len(recency_data)):
                RFM_result.append(
                {
                    "CustomerID": recency_data[i]["CustomerID"],
                    "total_score": recency_data[i]["recency_level"]*recency_weight + frequency_data[i]["frequency_level"]*frequency_weight + monetary_data[i]["monetary_level"]*monetary_weight,
                    "recency_score": recency_data[i]["recency_level"],
                    "frequency_score": frequency_data[i]["frequency_level"],
                    "monetary_score": monetary_data[i]["monetary_level"],
                })
            RFM_result = sorted(RFM_result, key = lambda x:x["total_score"], reverse=True)
            RFM_result = level(RFM_result, "RFM_group")
            RFM_result = sorted(RFM_result, key = lambda x:x["RFM_group"], reverse=True)
            print(RFM_result)
            # response_object['RFM'] = RFM_result
            # customer_info_list = RFM_result

            #寫入資料庫
            for i in RFM_result:
                update = f"""
                    UPDATE customer SET RFM = {i["RFM_group"]} WHERE CustomerID = {i["CustomerID"]} 
                """
                conn.execute(text(update))
                conn.execute(text("COMMIT;"))
        except Exception as e:
            response_object['status'] = "failure"
            response_object['message'] = str(e)
            print(str(e))
            return jsonify(response_object)
    
    # get LTV
    def get_LTV(year, rate, current_month):

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
                SELECT o.CustomerID, sum(t.Price) as total_price FROM orders as o
                JOIN ticketprice as t
                ON o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID
                WHERE (o.Date BETWEEN '{year}/{quarter * 3 - 2}/1' AND '{year}/{quarter * 3}/31')
                GROUP BY o.CustomerID;
            """
            price_data = query2dict(query, conn)

            for i in price_data:
                if i["total_price"] != None:
                    LTV = i["total_price"] * (1 - 1 / (1 + rate) ** 4) / rate
                else:
                    LTV = 0

                # for j in customer_info_list:
                #     if j["CustomerID"] == i["CustomerID"]:
                #         j["LTV"] = LTV
            
                update = f"""
                    UPDATE customer SET LTV = {LTV} WHERE CustomerID = {i["CustomerID"]};
                """
                conn.execute(text(update))
                conn.execute(text("COMMIT;"))        

        except Exception as e:
            response_object['status'] = "failure"
            response_object['message'] = str(e)
            print(str(e))
            return jsonify(response_object)


    # PCV
    def get_PCV(year, rate):
        try:
            query = f"""
                SELECT o.CustomerID, SUM(p.Price) AS PCV FROM orders o
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                JOIN customer
                WHERE o.Date BETWEEN '{year}/1/1' AND '{year}/12/31'
                GROUP BY CustomerID
                ORDER BY PCV DESC;
            """
            past_value_data = query2dict(query, conn)
            for i in past_value_data:
                i["PCV"] = i["PCV"]/(1+rate)
                # for j in customer_info_list:
                #     if j["CustomerID"] == i["CustomerID"]:
                #         j["PCV"] = i["PCV"]

            #寫入資料庫
                update = f"""
                    UPDATE customer SET PCV = {i["PCV"]} WHERE CustomerID = {i["CustomerID"]} 
                """
                conn.execute(text(update))
                conn.execute(text("COMMIT;"))

        except Exception as e:
            response_object['status'] = "failure"
            response_object['message'] = str(e)
            print(str(e))
            return jsonify(response_object)
        
    
    # 最後執行
    current_time = datetime.now()
    year = current_time.year
    current_month = current_time.month
    past_rate = 0.0125
    future_rate = 0.02
    get_RFM()
    get_LTV(year, future_rate, current_month)
    get_PCV(year, past_rate)

    try:
        query = f"""
            SELECT CustomerID, CONCAT(FirstName," ", LastName) Customer_name, Gender, PhoneNumber, Birthday, Email, Address, LTV, PCV, RFM FROM customer
            ORDER BY CustomerID;
        """
        customer_info_list = query2dict(query, conn)

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    # print(customer_info_list[0]["Birthday"])
    response_object['customer_info'] = customer_info_list

    return jsonify(response_object)
  
if __name__ == "__main__":
    app.run(debug=True)
