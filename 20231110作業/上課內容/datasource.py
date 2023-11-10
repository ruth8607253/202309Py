import requests
import psycopg2
import password

# 下載台北市youbike資料2.0
def download_youbike_data()->list[dict]:
    youbike_url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response = requests.get(youbike_url)
    response.raise_for_status()
    print("下載成功")
    return response.json()

def create_table(conn):    
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE  IF NOT EXISTS 台北市youbike(
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id" ),
            UNIQUE(站點名稱,更新時間)
        );
        '''
    )
    conn.commit()
    cursor.close()
    print("create table 成功")

def insert_data(conn,values:list[any])->None:
    cursor=conn.cursor()
    sql = '''
    INSERT INTO 台北市youbike(站點名稱,行政區,更新時間,地址,總車輛數,可借,可還)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (站點名稱,更新時間) DO NOTHING
    '''
    cursor.execute(sql,values)
    conn.commit()
    cursor.close()

def updata_render_data():
    data=download_youbike_data()
    conn=psycopg2.connect(database=password.database,
                            user=password.user,
                            password=password.password,
                            host=password.host,
                            port=password.port)
    
    create_table(conn)
    for item in data:
        insert_data(conn,[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
    conn.close()

def lastest_datetime_data()->list[tuple]:
    conn = psycopg2.connect(
                                database=password.database,
                                user=password.user,
                                password=password.password,
                                host=password.host,
                                port=password.port)
    cursor=conn.cursor()
    sql='''
    SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,地址,總車輛數,可借,可還
    FROM 台北市youbike 
    GROUP BY 站點名稱
    '''
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return rows