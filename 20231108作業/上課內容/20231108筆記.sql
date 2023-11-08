INSERT INTO 台北市youbike(站點名稱,更新時間,行政區,地址,總車輛數,可借,可還)
VALUES ('YouBike2.0_一壽橋','2023-11-01 17:38:19','文山區','樟新街64號前方',16,1,15)

SELECT * FROM 台北市youbike

COPY 台北市youbike FROM 'C:\YOUBIKE.csv' DELIMITER ',' CSV HEADER;

GRANT pg_read_server_files TO maindb;

CREATE TABLE  IF NOT EXISTS 台北市youbike(
            "id"	SERIAL,
            "站點名稱"	TEXT NOT NULL,
            "行政區"	TEXT NOT NULL,
            "更新時間"	TEXT NOT NULL,
            "地址"	TEXT,
            "總車輛數"	INTEGER,
            "可借"	INTEGER,
            "可還"	INTEGER,
            PRIMARY KEY("id"),
            UNIQUE(站點名稱,更新時間)
        );
