# 必要モジュールをインポートする
import sqlite3

# データベースに接続する
conn = sqlite3.connect('iungoback.db')
c = conn.cursor()

# テーブルの作成
c.execute('''CREATE TABLE dates(datetime text)''')

# 挿入した結果を保存（コミット）する
conn.commit()

# データベースへのアクセスが終わったら close する
conn.close()