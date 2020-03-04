import pandas as pd
import sqlite3

data = pd.read_csv('access.log52063'
                    , engine='python'
                    , sep=' '
                    , header=None
                    , names = ['IP', 'empty1', 'empty2', 'time', 'type', 'url', 'status', 'size', 'a']
                    )

con = sqlite3.connect("C:/workspace/Python/DB/log_analyze_db.db") #로그분석 DB파일 생성, 없으면 생성해주고 있으면 가져온다
cursor = con.cursor()


# 파일 전처리  : data 객체에서 초기값으로 들어온 객체를 하기의 항목으로 나눠서 임시 dataTemp 객체에 넣는다.
#  IP   : "15.3.3.1"
#  date : '20200101123160' --YYYYMMDDHHMMSS
#  P/G  : "POST"
#  URL  : "/portal/approval/work/getSoaUndoCount.do"
#  PROTOCOL : "HTTP/1.1 "
#  STATUS : 200
#  SIZE : 343
#  InpuDate :"20200302"

data.to_sql(name="TB_LOG", con=con, if_exists='append')

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
