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
import gurobipy as grb
import datetime as dt

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


@app.route('/revenue_analysis_backend', methods=['POST'])
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
        def movingAverage(date, Pdata, extraPeriod, n):
            predict_date = date.split("-")
            period = dt.date(int(predict_date[0]), int(predict_date[1]), int(predict_date[2])) - dt.date(2023, 2, 1)
            period = period.days

            data = Pdata['Price']
            length = len(data)

            data = np.append(data, [np.nan]*extraPeriod)
            forecast = np.full(length + extraPeriod, np.nan)

            for i in range(n, length):
                forecast[i] = np.mean(data[i-n:i])

            forecast[i+1:] = np.mean(data[i-n+1:i+1])

            if(period <= 5):
                return data[period]

            print(period)
            return forecast[period]
        

        def optimize(avg_Price):
            mSeat = grb.Model('Seat')
            seat_vars = {}
            order_vars = {}
            price_vars = {}

            for i in range(5):
                seat_vars[i]=mSeat.addVar(vtype=grb.GRB.INTEGER, name='x'+str(i+1))
            for i in range(5):
                price_vars[i]=mSeat.addVar(vtype=grb.GRB.INTEGER, name='p'+str(i+1))
            for i in range(5):
                order_vars[i]=mSeat.addVar(vtype=grb.GRB.INTEGER, name='y'+str(i+1))

            mSeat.addConstr((seat_vars[0]+seat_vars[1]+seat_vars[2]+seat_vars[3]+seat_vars[4])==180)
            mSeat.addConstr((order_vars[0]+order_vars[1]+order_vars[2]+order_vars[3]+order_vars[4])==180)

            mSeat.addConstr((seat_vars[0]+seat_vars[1]+seat_vars[2]+seat_vars[3]+seat_vars[4])>=order_vars[0])
            mSeat.addConstr((seat_vars[1]+seat_vars[2]+seat_vars[3]+seat_vars[4])>=order_vars[1])
            mSeat.addConstr((seat_vars[2]+seat_vars[3]+seat_vars[4])>=order_vars[2])
            mSeat.addConstr((seat_vars[3]+seat_vars[4])>=order_vars[3])
            mSeat.addConstr(seat_vars[4]>=order_vars[4])

            mSeat.addConstr(price_vars[0]>=7592)
            mSeat.addConstr(price_vars[1]>=6424)
            mSeat.addConstr(price_vars[2]>=5256)
            mSeat.addConstr(price_vars[3]>=4088)
            mSeat.addConstr(price_vars[4]>=2920)

            mSeat.addConstr(price_vars[0]<=8760)
            mSeat.addConstr(price_vars[1]<=7591)
            mSeat.addConstr(price_vars[2]<=6423)
            mSeat.addConstr(price_vars[3]<=5255)
            mSeat.addConstr(price_vars[4]<=4087)

            mSeat.addConstr(seat_vars[0]>=0)
            mSeat.addConstr(seat_vars[1]>=0)
            mSeat.addConstr(seat_vars[2]>=0)
            mSeat.addConstr(seat_vars[3]>=0)
            mSeat.addConstr(seat_vars[4]>=0)

            mSeat.addConstr(seat_vars[0]<=18)
            mSeat.addConstr(seat_vars[1]<=36)
            mSeat.addConstr(seat_vars[2]<=54)
            mSeat.addConstr(seat_vars[3]<=72)
            mSeat.addConstr(seat_vars[4]<=90)

            mSeat.addConstr(seat_vars[0]*price_vars[0]+seat_vars[1]*price_vars[1]+seat_vars[2]*price_vars[2]+seat_vars[3]*price_vars[3]+seat_vars[4]*price_vars[4]<=avg_Price*180)

            objective = seat_vars[0]*price_vars[0]+seat_vars[1]*price_vars[1]+seat_vars[2]*price_vars[2]+seat_vars[3]*price_vars[3]+seat_vars[4]*price_vars[4]
            mSeat.setObjective(objective,grb.GRB.MAXIMIZE)
            mSeat.update()
            mSeat.optimize()

            return mSeat
        
        
        def getSeatLevel(model):
            vars = model.getVars()
            seat_level = []
            for i in range(0,5):
                seat_level.append(vars[i].X)

            return seat_level
        
        
        def getPriceLevel(model):
            vars = model.getVars()
            price_level = []
            for i in range(5,10):
                price_level.append(vars[i].X)

            return price_level

        priceData = pd.read_csv("Ticket_Price.csv", encoding='unicode_escape')
        avg_price = movingAverage("2023-7-25", priceData, 5, 5)
        model = optimize(avg_price)
        
        #測試資料
        test_avaerge_daily_price = avg_price
        test_seat_level_num = getSeatLevel(model)
        test_price_level = getPriceLevel(model)

        print(test_price_level)
        print(test_seat_level_num)

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

@app.route('/get_sales_rate', methods=['POST'])
def get_sales_rate():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    post_data = request.get_json()
    flight_code = post_data.get("flight_code")
    time = post_data.get("time")
    year = ['2023']
    
    try:
        querySeat = f"""
            SELECT a.SeatNumber 
            FROM flight as f
            JOIN airplanetype as a 
            ON f.AirplaneTypeID = a.AirplaneTypeID
            WHERE f.FlightCode = '{flight_code}';
        """
        seat_num = query2dict(querySeat, conn)
        sales_list = []

        if time == "月":
            if flight_code == "全部":
                for y in year:
                    for i in range(1, 13):
                        if i == 2:
                            query = f"""
                                SELECT COUNT(o.OrderID) FROM orders o 
                                WHERE o.FlightCode = '{flight_code}'                              
                                AND o.Status = 'OK'
                                AND o.Date BETWEEN '{y}/{i}/1' AND '{y}/{i}/28'
                                GROUP BY o.OrderID;
                            """
                        else:
                            query = f"""
                                SELECT COUNT(o.OrderID) count FROM orders o 
                                WHERE o.FlightCode = '{flight_code}'                              
                                AND o.Status = 'OK'
                                AND o.Date BETWEEN '{y}/{i}/1' AND '{y}/{i}/30'
                                GROUP BY o.OrderID;
                            """
                        sales_num = query2dict(query, conn)
                        if len(sales_num) == 0:
                            sales_rate = 0
                        else:
                            sales = 0
                            for num in sales_num:
                                sales += num["count"] 
                            sales_rate = sales / seat_num[0]["SeatNumber"]
                        sales_list.append({f"{y}/{i}": sales_rate})
                
                response_object['sales_rate_list'] = sales_list

            else:               
                for y in year:
                    for i in range(1, 13):
                        if i == 2:
                            query = f"""
                                SELECT COUNT(o.OrderID) count FROM orders o
                                JOIN flight f
                                ON o.FlightID = f.FlightID
                                WHERE f.FlightCode = '{flight_code}'                             
                                AND o.Status = 'OK'
                                AND o.Date BETWEEN '{y}/{i}/1' AND '{y}/{i}/28'
                                GROUP BY o.OrderID;
                            """
                        else:
                            query = f"""
                                SELECT COUNT(o.OrderID) count FROM orders o
                                JOIN flight f
                                ON o.FlightID = f.FlightID
                                WHERE f.FlightCode = '{flight_code}'                             
                                AND o.Status = 'OK'
                                AND o.Date BETWEEN '{y}/{i}/1' AND '{y}/{i}/30'
                                GROUP BY o.OrderID;
                            """
                        sales_num = query2dict(query, conn)
                        if len(sales_num) == 0:
                            sales_rate = 0
                        else:
                            sales = 0
                            for num in sales_num:
                                sales += num["count"] 
                            sales_rate = sales / seat_num[0]["SeatNumber"]
                        sales_list.append({f"{y}/{i}": sales_rate})
                
                response_object['sales_rate_list'] = sales_list

        elif time == "季":
            for y in year:
                for i in range(1, 5):

                    query = f"""
                        SELECT COUNT(o.OrderID) count FROM orders o
                        JOIN flight f
                        ON o.FlightID = f.FlightID
                        WHERE f.FlightCode = '{flight_code}'                             
                        AND o.Status = 'OK'
                        AND o.Date BETWEEN '{y}/{i*3-2}/1' AND '{y}/{i*3}/30'
                        GROUP BY o.OrderID;
                    """

                    sales_num = query2dict(query, conn)
                    if len(sales_num) == 0:
                        sales_rate = 0
                    else:
                        sales = 0
                        for num in sales_num:
                            sales += num["count"] 
                        sales_rate = sales / seat_num[0]["SeatNumber"]
                    sales_list.append({f"{y} Q{i}": sales_rate})
                
            response_object['sales_rate_list'] = sales_list

        elif time == "年":
            for y in year:
                query = f"""
                        SELECT COUNT(o.OrderID) count FROM orders o
                        JOIN flight f
                        ON o.FlightID = f.FlightID
                        WHERE f.FlightCode = '{flight_code}'                             
                        AND o.Status = 'OK'
                        AND o.Date BETWEEN '{y}/1/1' AND '{y}/12/31'
                        GROUP BY o.OrderID;
                    """

                sales_num = query2dict(query, conn)
                if len(sales_num) == 0:
                    sales_rate = 0
                else:
                    sales = 0
                    for num in sales_num:
                        sales += num["count"] 
                    sales_rate = sales / seat_num[0]["SeatNumber"]
                sales_list.append({f"{y}": sales_rate})
                
            response_object['sales_rate_list'] = sales_list
        
    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(e)
        return jsonify(response_object)
    
    response_object['message'] = f"成功搜尋{flight_code}的售票率 以{time}為單位"
    conn.close()
    
    return jsonify(response_object)

@app.route('/get_all_flight_code', methods=['GET'])
def get_all_flight_code():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    try:
        query = """
            SELECT FlightID, FlightCode FROM flight;
        """
        data = query2dict(query, conn)
        response_object['flight_code'] = data
    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
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
                SELECT o.CustomerId, CONCAT(c.FirstName, " ", c.LastName) CustomerName, f.FlightCode, p.Price, o.PriceLevel, o.Date, f.Origin, f.Destination FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                WHERE f.FlightID = "{flight_id}"
                AND o.Date = "{date}"
                AND o.Status = "OK";
            """
        elif date != None:
            query = f"""
                SELECT o.CustomerId, CONCAT(c.FirstName, " ", c.LastName) CustomerName, f.FlightCode, p.Price, o.PriceLevel, o.Date, f.Origin, f.Destination FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                WHERE o.Date = "{date}"
                AND o.Status = "OK";
            """
        elif flight_id != None:
            query = f"""
                SELECT o.CustomerId, CONCAT(c.FirstName, " ", c.LastName) CustomerName, f.FlightCode, p.Price, o.PriceLevel, o.Date, f.Origin, f.Destination FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
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
                SELECT o.CustomerId, CONCAT(c.FirstName, " ", c.LastName) CustomerName, f.FlightCode, p.Price, o.PriceLevel, o.Date, f.Origin, f.Destination FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                WHERE f.FlightID = "{flight_id}"
                AND o.Date = "{date}"
                AND o.Status = "Cancel";
            """
        elif date != None:
            query = f"""
                SELECT o.CustomerId, CONCAT(c.FirstName, " ", c.LastName) CustomerName, f.FlightCode, p.Price, o.PriceLevel, o.Date, f.Origin, f.Destination FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
                WHERE o.Date = "{date}"
                AND o.Status = "Cancel";
            """
        elif flight_id != None:
            query = f"""
                SELECT o.CustomerId, CONCAT(c.FirstName, " ", c.LastName) CustomerName, f.FlightCode, p.Price, o.PriceLevel, o.Date, f.Origin, f.Destination FROM orders o
                JOIN flight f
                ON o.FlightID = f.FlightID
                JOIN customer c
                ON c.CustomerID = o.CustomerID
                JOIN ticketprice p
                ON (o.PriceLevel = p.PriceLevel AND o.Date = p.Date AND o.FlightID = p.FlightID)
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

            dictLTV = {"CustomerID" : i, "LTV" : str(round(LTV, 5))}
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

# 單期的留存率
@app.route('/get_single_retention_rate', methods=['POST'])
def get_single_retention_rate():
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
            dictRR = {"retention rate" : retRate}
            RRlist = [dictRR]
            response_object['retention rate'] = RRlist
        else:
            retRate = count_cur / count_last
            dictRR = {"retention rate" : retRate}
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

# 全部期的留存率
@app.route('/get_retention_rate', methods=['GET'])
def get_retention_rate():
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
            
            dictRR = {"{} Q{}".format(str(year), str(i)) : retRate}
            RRlist.append(dictRR)

        response_object['year'] = year
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

# 單期的存活率
@app.route('/get_single_survival_rate', methods=['POST'])
def get_single_survival_rate():
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
                dictSR = {"survival rate" : surRate}
                SRlist = [dictSR]
                response_object['survival rate'] = SRlist
                break
            else:
                retRate = count_cur / count_last
                surRate *= retRate
                dictSR = {"survival rate" : surRate}
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

# 全部期的存活率
@app.route('/get_survival_rate', methods=['GET'])
def get_survival_rate():
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
            
            dictSR = {"{} Q{}".format(str(year), str(i)) : surRate}
            SRlist.append(dictSR)

        response_object['year'] = year
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


@app.route('/get_left_seat', methods=['POST'])
def get_left_seat():
    response_object = {'status': 'success'}
    
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    post_data = request.get_json()
    flightID = post_data.get("flightID")
    date = post_data.get("date")
    
    try:
        # 抓座位數
        querySeat = f"""
            SELECT a.SeatNumber FROM flight as f, airplanetype as a 
            WHERE f.AirplaneTypeID = a.AirplaneTypeID AND f.FlightID = {flightID};
        """

        result_seat = conn.execute(text(querySeat))
        row_seat = result_seat.fetchone()
        seatNumber = int(row_seat[0])

        # 獲取哪些座位被預訂
        query = f"""
            SELECT o.SeatID FROM orders o WHERE o.FlightID = {flightID} AND o.Date = "{date}" AND o.Status = 'OK';
        """

        result = conn.execute(text(query))
        ordered_seat = []
        for row in result.fetchall():
            ordered_seat.append(int(row[0]))

        # 獲取尚未被預訂的座位
        vacant = []
        for i in range(1, seatNumber + 1):
            if(i in ordered_seat) == False:
                vacant.append(i)

        ordered_num = len(ordered_seat)
        vacant_num = len(vacant)

        # 被預定百分比/售票狀況
        ratio = ordered_num / seatNumber
        ratio = round(ratio, 4)

        response_object['ordered_seat_list'] = ordered_seat
        response_object['vacant_list'] = vacant
        response_object['ordered_num'] = ordered_num
        response_object['vacant_num'] = vacant_num
        response_object['ordered_ratio'] = ratio

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"成功搜尋{date}的剩餘機位"
    result_seat.close()
    result.close()
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
    print(customer_info_list)
    response_object['customer_info'] = customer_info_list

    return jsonify(response_object)


@app.route('/CE', methods=['GET'])
def CE():
    response_object = {'status': 'success'}
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    year = 2023
    rate = 0.02

    # 算LTV
    def calLTV(year, rate):
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
            
                update = f"""
                    UPDATE customer SET LTV = {LTV} WHERE CustomerID = {i};
                """
                conn.execute(text(update))
                conn.execute(text("COMMIT;"))

        except Exception as e:
            response_object['status'] = "failure"
            response_object['message'] = str(e)
            print(str(e))
            return jsonify(response_object)
        
        result.close()
        countResult.close()
        conn.close()

    calLTV(year, rate)

    try:
        query = f"""
            SELECT sum(LTV) FROM customer;
        """

        result = conn.execute(text(query))
        row = result.fetchone()
        ce = row[0]

        dictCE = {"customer equity" : ce}
        CElist = [dictCE]
        response_object['customer equity'] = CElist

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)

    response_object['message'] = f"成功搜尋CE"
    result.close()
    conn.close()
    
    return jsonify(response_object)


@app.route('/region_rank', methods = ['POST'])
def region_rank():
    response_object = {'status': 'success'}
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    post_data = request.get_json()
    time = post_data.get("time")
    rank_list = []
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day

    try:
        if time == "週":
            if day > 7:
                query = f"""
                    SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                    JOIN orders o ON c.CustomerID = o.CustomerID
                    JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                    WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month}/{day - 7}' AND '{year}/{month}/{day - 1}' 
                    GROUP BY City ORDER BY Total DESC LIMIT 5;
                """

                query_all = f"""
                    SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                    JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                    WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month}/{day - 7}' AND '{year}/{month}/{day - 1}';
                """

            elif day == 1:
                query = f"""
                    SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                    JOIN orders o ON c.CustomerID = o.CustomerID
                    JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                    WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month - 1}/24' AND '{year}/{month - 1}/30' 
                    GROUP BY City ORDER BY Total DESC LIMIT 5;
                """

                query_all = f"""
                    SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                    JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                    WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month - 1}/24' AND '{year}/{month - 1}/30';
                """

            else:
                query = f"""
                    SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                    JOIN orders o ON c.CustomerID = o.CustomerID
                    JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                    WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month - 1}/{day + 23}' AND '{year}/{month}/{day - 1}' 
                    GROUP BY City ORDER BY Total DESC LIMIT 5;
                """

                query_all = f"""
                    SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                    JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                    WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month - 1}/{day + 23}' AND '{year}/{month}/{day - 1}';
                """

        elif time == "月":
            query = f"""
                SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month}/1' AND '{year}/{month}/30' 
                GROUP BY City ORDER BY Total DESC LIMIT 5;
            """

            query_all = f"""
                SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{month}/1' AND '{year}/{month}/30';
            """

        elif time == "季":
            if month <= 3:
                quarter = 1
            elif month <=6:
                quarter = 2
            elif month <= 9:
                quarter = 3
            else:
                quarter = 4

            query = f"""
                SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{quarter * 3 - 2}/1' AND '{year}/{quarter * 3}/30' 
                GROUP BY City ORDER BY Total DESC LIMIT 5;
            """

            query_all = f"""
                SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/{quarter * 3 - 2}/1' AND '{year}/{quarter * 3}/30';
            """
            
        elif time == "年":
            query = f"""
                SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/1/1' AND '{year}/12/31' 
                GROUP BY City ORDER BY Total DESC LIMIT 5;
            """

            query_all = f"""
                SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' AND o.Date BETWEEN '{year}/1/1' AND '{year}/12/31';
            """

        else:  # 全部(不篩時間)，保險用
            query = f"""
                SELECT SUBSTRING(c.Address, 1, 3) AS City, SUM(t.Price * o.Amount) AS Total FROM customer c
                JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK' GROUP BY City ORDER BY Total DESC LIMIT 5;
            """

            query_all = f"""
                SELECT SUM(t.Price * o.Amount) FROM customer c JOIN orders o ON c.CustomerID = o.CustomerID
                JOIN ticketprice t ON (o.Date = t.Date AND o.PriceLevel = t.PriceLevel AND o.FlightID = t.FlightID)
                WHERE o.Status = 'OK';
            """

        result = conn.execute(text(query))
        result_all = conn.execute(text(query_all))
        total = int(result_all.fetchone()[0]) # 全部城市的貢獻

        i = 1
        sum = 0
        for row in result.fetchall():
            ratio = int(row[1]) / total
            rankDict = {"rank" : str(i), "region" : row[0], "rate" : str(round(ratio * 100, 2)) + "%", "value" : row[1]}
            rank_list.append(rankDict)
            sum += int(row[1])
            i += 1

        rest = {"rank" : "6", "region" : "其他", "rate" : str(round((total - sum) / total * 100, 2)) + "%", "value" : float(total - sum)}
        rank_list.append(rest)

        response_object['rank'] = rank_list

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"貢獻度前五高的城市"
    result.close()
    result_all.close()
    conn.close()
    
    return jsonify(response_object)


@app.route('/class_rank', methods = ['POST'])
def class_rank():
    response_object = {'status': 'success'}
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)
    
    post_data = request.get_json()
    time = post_data.get("time")
    rank_list = []
    current_time = datetime.now()
    year = current_time.year
    month = current_time.month
    day = current_time.day
    # day = 8

    try:
        if time == "週":
            if day > 7:
                query = f"""
                    SELECT t.PriceLevel, SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                    WHERE t.Date BETWEEN '{year}/{month}/{day - 7}' AND '{year}/{month}/{day - 1}' 
                    GROUP BY t.PriceLevel ORDER BY Total DESC;
                """

                query_all = f"""
                    SELECT SUM(t.Price * t.Amount) FROM ticketprice t 
                    WHERE t.Date BETWEEN '{year}/{month}/{day - 7}' AND '{year}/{month}/{day - 1}';
                """
            elif day == 1:
                query = f"""
                    SELECT t.PriceLevel, SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                    WHERE t.Date BETWEEN '{year}/{month - 1}/24' AND '{year}/{month - 1}/30' 
                    GROUP BY t.PriceLevel ORDER BY Total DESC;
                """

                query_all = f"""
                    SELECT SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                    WHERE t.Date BETWEEN '{year}/{month - 1}/24' AND '{year}/{month - 1}/30';
                """
            else:
                query = f"""
                    SELECT t.PriceLevel, SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                    WHERE t.Date BETWEEN '{year}/{month - 1}/{day + 23}' AND '{year}/{month}/{day - 1}' 
                    GROUP BY t.PriceLevel ORDER BY Total DESC;
                """

                query_all = f"""
                    SELECT SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                    WHERE t.Date BETWEEN '{year}/{month - 1}/{day + 23}' AND '{year}/{month}/{day - 1}';
                """
            
        else: # 單日
            query = f"""
                SELECT t.PriceLevel, SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                WHERE t.Date = '{year}/{month}/{day}'
                GROUP BY t.PriceLevel ORDER BY Total DESC;
            """

            query_all = f"""
                SELECT SUM(t.Price * t.Amount) AS Total FROM ticketprice t 
                WHERE t.Date = '{year}/{month}/{day}';
            """

        result = conn.execute(text(query))
        result_all = conn.execute(text(query_all))
        total = int(result_all.fetchone()[0]) # 全部艙位的貢獻

        for row in result.fetchall():
            rankDict = {"class" : row[0], "rate" : str(round((int(row[1]) / total) * 100, 2)) + "%", "value" : row[1]}
            rank_list.append(rankDict)

        response_object['rank'] = rank_list

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"艙位貢獻比例"
    result.close()
    conn.close()
    
    return jsonify(response_object)


@app.route('/booking', methods = ['POST'])
def booking():
    response_object = {'status': 'success'}
    try:
        conn = engine.connect()
    except:
        response_object['status'] = "failure"
        response_object['message'] = "資料庫連線失敗"
        return jsonify(response_object)

    post_data = request.get_json()
    origin = post_data.get("origin")
    dest = post_data.get("destination")
    dep_date = post_data.get("department_date")
    # back_date = post_data.get("back_date")
    amount = post_data.get("amount")
    seat = post_data.get("seat")

    custID = 1

    try:
        # 抓航班ID
        query = f"""
            SELECT FlightID FROM flight WHERE Origin = '{origin}' AND Destination = '{dest}';
        """
        result = conn.execute(text(query))
        row = result.fetchone()
        id = int(row[0])

        insert = f"""
            INSERT INTO orders ('Date', 'PriceLevel', 'SeatID', 'CustomerID', 'FlightID', 'Amount', 'Status') 
            VALUES ("{dep_date}", "A", {seat}, {custID}, {id}, {amount}, "OK");
        """
        conn.execute(text(insert))
        conn.execute(text("COMMIT;"))

    except Exception as e:
        response_object['status'] = "failure"
        response_object['message'] = str(e)
        print(str(e))
        return jsonify(response_object)
    
    response_object['message'] = f"成功訂位"
    result.close()
    conn.close()
    
    return jsonify(response_object)

  
if __name__ == "__main__":
    app.run(debug=True)