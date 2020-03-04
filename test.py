import pandas as pd
import sqlite3

data = pd.read_csv('access.log52063'
                    , engine='python'
                    , sep=' '
                    , header=None
                    , names = ['ip', 'empty1', 'empty2', 'time', 'type', 'url', 'status', 'size', 'a']
                    )

con = sqlite3.connect("C:/workspace/Python/Pyth37Start/python-studylog_analyze_db.db") #로그분석 DB파일 생성, 없으면 생성해주고 있으면 가져온다
cursor = con.cursor()

#sql = "CREATE TABLE ACCESS_LOG(IP TEXT, TIME TEXT, TYPE TEXT, URL TEXT, STATUS INTEGER, SIZE INTEGER)"
#cursor.execute(sql)
#AAAAAAAAffffffff
print(data[['ip', 'time']])

#sql = "INSERT INTO ACCESS_LOG VALUES('10.60.30.68', '2020-02-17', 'GET', 'www.ourhome.co.kr', 200, 10)"
#cursor.execute(sql)

sql = "SELECT * FROM ACCESS_LOG"
#print(cursor.execute(sql).fetchall())

con.commit()
con.close()

