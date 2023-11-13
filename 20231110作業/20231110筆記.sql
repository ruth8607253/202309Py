INSERT INTO 台北市youbike (站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還) 
VALUES ('YouBike2.0_一壽橋','文山區','2023-11-08 10:43:16','樟新街64號前方',0,0,0)
ON CONFLICT (站點名稱,更新時間) DO nothing
  SET 總車輛數 = 100, 
      可借 = 100,
	  可還 = 100;
	  
	  
SELECT * 
FROM 台北市youbike

SELECT 站點名稱,MAX(更新時間) AS 更新時間,行政區, 地址, 總車輛數, 可借, 可還\
FROM 台北市youbike
WHERE 更新時間 (
	SELECT MAX(更新時間)
	FROM 台北市youbike
	GROUP BY 站點名稱
	)
GROUP BY 站點名稱, 行政區, 更新時間, 地址, 總車輛數, 可借, 可還