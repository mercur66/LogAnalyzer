import pandas as pd
import sqlite3
from datetime import datetime
import moduleFun as md

data = pd.read_csv('access.log52063'
                    , engine='python'
                    , sep=' '
                    , header=None
                    , names = ['IP', 'empty1', 'empty2', 'time', 'type', 'url', 'status', 'size', 'a']
                    )

con = sqlite3.connect("C:/workspace/Python/DB/log_analyze_db.db") #로그분석 DB파일 생성, 없으면 생성해주고 있으면 가져온다
cursor = con.cursor()

# data.to_sql(name="TB_LOG", con=con, if_exists='replace')

# if_exits
# fail: Raise a ValueError.
# replace: Drop the table before inserting new values.#
# append: Insert new values to the existing table.

sql = "SELECT * FROM TB_LOG where rowid <= 10 "
# cursor.execute(sql).fetchall()
cursor.execute(sql)

for row in cursor:
    print("===========================================")

    print(row)

    vTemp = row[4].split('/')
    vDay = vTemp[0].replace('[','')
    vMon = md.cvMonthNum(vTemp[1])
    vYear = vTemp[2].split(':')[0]
    vHH = vTemp[2].split(':')[1]
    vMM = vTemp[2].split(':')[2]
    vSS = vTemp[2].split(':')[3]

    splitURL = row[6].split()

    vIp = row[1]
    vDateTime =  vYear+vMon+vDay+vHH+vMM+vSS
    timeZone = row[5].replace(']', '')
    vPG = splitURL[0]
    vURL = splitURL[1]
    vProtocol = splitURL[2]
    vStatus = row[7]
    vSize = row[8]
    vNowDate = datetime.today().strftime("%Y%m%d%H%M%S")



    print("IP : " + vIp)
    print("DateTime : " + vDateTime )
    print("timeZone : " + timeZone)
    print("P/G : " + vPG )
    print("URL : " + vURL)
    print("PROTOCOL  : " + vProtocol)
    print("STATUS : " + str(vStatus))
    print("SIZE : " + str(vSize))
    print("Now : " + vNowDate)

    print("===========================================")

# 파일 전처리  : data 객체에서 초기값으로 들어온 객체를 하기의 항목으로 나눠서 임시 dataTemp 객체에 넣는다.
#  IP   : "15.3.3.1"
#  date : '20200101123160' --YYYYMMDDHHMMSS
#  P/G  : "POST"
#  URL  : "/portal/approval/work/getSoaUndoCount.do"
#  PROTOCOL : "HTTP/1.1 "
#  STATUS : 200
#  SIZE : 343
#  InpuDate :"20200302"

con.commit()
con.close()

#
# con = sqlite3.connect("C:/workspace/Python/DB/log_analyze_db.db") #로그분석 DB파일 생성, 없으면 생성해주고 있으면 가져온다
# cursor = con.cursor()
#
# sql = "CREATE TABLE ACCESS_LOG(IP TEXT, TIME TEXT, TYPE TEXT, URL TEXT, STATUS INTEGER, SIZE INTEGER)"
# cursor.execute(sql)
# #AAAAAAAAffffffff
# print(data[['ip', 'time']])
#
# sql = "INSERT INTO ACCESS_LOG VALUES('10.60.30.68', '2020-02-17', 'GET', 'www.ourhome.co.kr', 200, 10)"
# cursor.execute(sql)
#
# sql = "SELECT * FROM ACCESS_LOG"
# cursor.execute(sql).fetchall()

# con.commit()
# con.close()
#
