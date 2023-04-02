import pandas as pd
import pymysql as pms
conn = pms.connect(host="localhost",
                   port=3306,
                   user="root",
                   password="samsql123",
                   db="ml_cia2")
cur = conn.cursor()
cur.execute("select * from details")
output = cur.fetchall()
print(output)

sql = "select * from details"
df = pd.read_sql(sql, conn)
