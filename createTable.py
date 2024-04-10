import sqlite3
db_connect = sqlite3.connect('sqlite_test.db')

# カーソル呼び出し
db_curs = db_connect.cursor()

# テーブル作成の命令をSQLにて指示
sql = 'CREATE TABLE human_sensor(id INTEGER PRIMARY KEY AUTOINCREMENT, high_date TEXT)'
db_curs.execute(sql)

# 実行
db_connect.commit()

db_connect.close()