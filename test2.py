import pandas as pd
import sqlite3
import os
from pm4py.objects.log.adapters.pandas import csv_import_adapter
import datetime

data = pd.read_csv('access.log52063'
                    , engine='python'
                    , sep=' '
                    , header=None
                    , names = ['ip', 'empty1', 'empty2', 'time', 'empty3', 'pre_url', 'status', 'size', 'empty4']
                    , parse_dates=['time']
                    )

dataTemp = data.drop(['empty1', 'empty2', 'empty3', 'empty4'], axis='columns') #불필요한 컬럼 제거
dataTemp['time'] = dataTemp['time'].str.replace('[', '')
dataTemp['time'] = pd.to_datetime(dataTemp['time'], format='%d/%b/%Y:%H:%M:%S') #datetime 형식으로 형변환
dataTemp[['pg', 'url', 'protocol']] = dataTemp['pre_url'].str.split(' ', n=2, expand=True) #url 컬럼 분할
dataTemp = dataTemp.drop(['pre_url'], axis='columns') #기존 url 삭제

dataTemp.rename(columns={'ip': 'case:concept:name', 'url': 'concept:name', 'time': 'time:timestamp'}, inplace=True)

print(dataTemp['concept:name'][0])
print(dataTemp['case:concept:name'][0])
print(dataTemp['time:timestamp'][0])
print(type(dataTemp['time:timestamp'][0]))