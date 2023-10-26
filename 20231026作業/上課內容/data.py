import requests
import sqlite3

__all__=["SQL"] # 這是我這個套件最終的執行結果

# 下載youbike data
def __download()->list[dict]:
    data_url="https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    response=requests.get(data_url)
    # 檢查是否下載成功方法1：raise_for_status
    response.raise_for_status()
    print("下載成功")
    return response.json()

    '''
    # 檢查是否下載成功方法2：status_code
    if response.status_code == 200: #-> 成功
        raise Exception("下載成功")
    else:
        raise Exception("下載失敗")
    '''

#創建SQL的table
def __table(con:sqlite3.Connection):
    # con=sqlite3.connect("a.db") #如果沒有就建一個新的，有就用原本那個檔
    cur=con.cursor()
    cur.execute(
        '''
        CREATE TABLE IF NOT EXISTS 台北市(
            "ID"	INTEGER,
            "區域"	TEXT NOT NULL,
            "站點名稱"	TEXT NOT NULL,
            "目前車輛數量"	INTEGER NOT NULL,
            "空位數量"	INTEGER NOT NULL,
            "總停車格"	INTEGER NOT NULL,
            "地址"	TEXT NOT NULL,
            "資料更新時間"	TEXT NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT),
            UNQIUE("站點名稱","資料更新時間") ON CONFLICT PREPLACE
        );
        '''
    )
    con.commit()

# 輸入資料到SQLlite裡
def __input_data(con:sqlite3.Connection,values:list[any])->None: #不會傳出東西
	cur=con.cursor()
	sql='''
	REPLACE INTO 台北市(區域,站點名稱,目前車輛數量,空位數量,總停車格,地址,資料更新時間)
	values(?,?,?,?,?,?,?)
	'''
	cur.execute(sql,values)
	con.commit()
 



#更新並把資料存進SQLlite
def SQL():
    data=__download()
    con=sqlite3.connect("a.db")
    __table(con)
    for item in data:
        __input_data(con,[item["sarea"],item["sna"],item["sbi"],item["bemp"],item["tot"],item["ar"],item["mday"]])
    con.close()