#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import datetime
import quandl
import pandas as pd
import sqlalchemy as sa
# 各種設定
## 取得したい日付レンジの指定
start = datetime.datetime(2007, 1, 1)
end = datetime.datetime(2019, 1, 19)

# 取得したい会社のティックシンボルを記載します。
## 例えばの武田薬品工業の場合　TSE/4502 となります。
## https://www.quandl.com/data/TSE/4502-Takeda-Pharmaceutical-Co-Ltd-4502
company_id = 'TSE/4502'

# APIキーの設定
quandl.ApiConfig.api_key = '×××××××××××××××××''

# データ取得
df = quandl.get(company_id ,start_date=start,end_date=end)

print(df.head())
## Indexが日付なので行に取り込んで、データ型を変更する。
df = df.reset_index()
df['Date'] = pd.to_datetime(df['Date'])

## 表名の指定
table_name = 'TAKEDA'

## 接続情報設定
engine = sa.create_engine('mysql+mysqlconnector://stock:stock@127.0.0.1/stock', echo=True)

# MySQLにデータを格納
df.to_sql(table_name, engine , index=False, if_exists='replace')
