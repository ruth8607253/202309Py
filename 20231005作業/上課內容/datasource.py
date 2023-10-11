import requests
import csv
import io

def __download()->list[list]:
    # 111年台灣各縣市人口密度
    url="https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108"

    a=requests.request("GET",url)

    try:
        a.raise_for_status()
    except:
        raise Exception("連線發生錯誤，網路中斷")
    else:
        if not a.ok:
            raise Exception("下載失敗，伺服器錯誤訊息")
        else:
            file = io.StringIO(a.text)
            a_reader=csv.reader(file)
            next(a_reader)
            return list(a_reader)

def cities_info()->list[list]:
    cities=[]
    try:
        a_list=__download()
    except Exception as i:
        print(f"錯誤：{i}")
    else:
        for i in a_list:
            if i[0] =='111':
                cities.append(i)
    return cities