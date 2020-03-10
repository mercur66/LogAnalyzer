import pandas as pd
import sqlite3
import datetime

data = pd.read_csv('access.log52063'
                    , engine='python'
                    , sep=' '
                    , header=None
                    , names = ['IP', 'empty1', 'empty2', 'time', 'empty3', 'pre_url', 'status', 'size', 'empty4']
                    , parse_dates=['time']
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

#데이터 프레임 조작 문법 https://blog.naver.com/vi_football/221666988299

#print(data)
dataTemp = data.drop(['empty1', 'empty2', 'empty3', 'empty4'], axis='columns') #불필요한 컬럼 제거
dataTemp['time'] = dataTemp['time'].str.replace('[', '')
dataTemp['time'] = pd.to_datetime(dataTemp['time'], format='%d/%b/%Y:%H:%M:%S') #datetime 형식으로 형변환
dataTemp[['pg', 'url', 'protocol']] = dataTemp['pre_url'].str.split(' ', n=2, expand=True) #url 컬럼 분할
dataTemp = dataTemp.drop(['pre_url'], axis='columns') #기존 url 삭제
#print(datetime.datetime.now())
#print(dataTemp)
dataTemp.to_sql(name="TB_LOG", con=con, if_exists='replace') #DB 에 저장

con.commit()
con.close()
