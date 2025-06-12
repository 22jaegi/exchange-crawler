import time
import subprocess

while True:
    subprocess.run(["python", "crawler/get_usd.py"])
    print("✅ 크롤 완료. 10초 대기 중...\n")
    time.sleep(10)
