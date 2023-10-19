'''
print("歡迎使用自我介紹產生器")
print("大家好我是"+input("請輸入您的名字：")+"，今年"+input("請輸入您的年紀：")+"歲，我很喜歡"+input("請輸入您的興趣：")+"，很高興認識大家！")
#1:06:32開始'''

import requests
import yfinance as yf
import csv
import pandas as pd
from io import StringIO
import pandas as pd
import sqlite3
import json

dat = yf.download("0050.TW", start="2023-01-01")
data_csv = dat.to_csv()
csv_data = pd.read_csv(StringIO(data_csv))
int_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
csv_data[int_columns] = csv_data[int_columns].astype(float)
csv_data.to_json('0050.json',orient="records")


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS 元大50 (
            "日期" REAL,
            "開盤價" REAL,
            "盤中最高價" REAL,
            "盤中最低價" REAL,
            "收盤價" REAL,
            "調整後收盤價" REAL,
            "成交量" REAL
        );
        '''
    )
    conn.commit()

def insert_data(conn):
    with open("0050.json", "r") as file:
        data = json.load(file)

    cursor = conn.cursor()
    for entry in data:
        cursor.execute(
            '''
            INSERT INTO 元大50 (日期, 開盤價, 盤中最高價, 盤中最低價, 收盤價, 調整後收盤價, 成交量)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            ''',
            (entry["Date"], entry["Open"], entry["High"], entry["Low"], entry["Close"], entry["Adj Close"], entry["Volume"])
        
        )
    conn.commit()

conn = sqlite3.connect("0050.db")

create_table(conn)

insert_data(conn)

conn.close()