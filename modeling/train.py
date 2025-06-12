import MySQLdb
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

conn = MySQLdb.connect(
    user="root", passwd="0000", host="127.0.0.1", db="exchange_db", charset="utf8"
)
cur = conn.cursor()
cur.execute("SELECT id, usd_rate FROM usd_exchange ORDER BY id DESC LIMIT 20")
rows = cur.fetchall()[::-1]

X = np.array([[r[0]] for r in rows])
y = np.array([r[1] for r in rows])

model = LinearRegression().fit(X, y)
joblib.dump(model, "modeling/model.pkl")
conn.close()
