-- 抓站點名稱的資料-----------------------
SELECT 站點名稱 
FROM 台北市youbike

-- DISTINCT：抓不重複的資料----------------
SELECT DISTINCT 站點名稱 
FROM 台北市youbike 

-- 按時間排序，最新放前面
SELECT DISTINCT 站點名稱,更新時間 
FROM 台北市youbike 
ORDER BY 更新時間 
DESC LIMIT 1320 

-- 抓最新資料------------------------------
SELECT 站點名稱,MAX(更新時間) AS 更新時間
FROM 台北市youbike 
GROUP BY 站點名稱

-- XXX------------------------------
SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區,更新時間,地址,總車輛數,可借,可還
FROM 台北市youbike 
GROUP BY 站點名稱
HAVING 站點名稱 LIKE '%振興%'