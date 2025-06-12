import requests
from bs4 import BeautifulSoup
from datetime import datetime
import MySQLdb

# 환율 크롤링
url = "https://finance.naver.com/marketindex/"
res = requests.get(url)
res.encoding = "euc-kr"
soup = BeautifulSoup(res.text, "html.parser")
usd = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value")

rate = float(usd.text.replace(",", ""))
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"💵 {now} - USD 환율: {rate} 원")

# DB 저장
conn = MySQLdb.connect(
    user="root",
    passwd="0000",
    host="127.0.0.1",  # ← 중요! localhost 대신 이거 써
    db="exchange_db",
    charset="utf8",
)

cur = conn.cursor()
sql = "INSERT INTO usd_exchange (datetime, usd_rate) VALUES (%s, %s)"
cur.execute(sql, (now, rate))
conn.commit()
conn.close()
