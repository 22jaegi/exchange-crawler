# 💵 USD 환율 예측 웹 서비스

실시간으로 미국 달러(USD) 환율을 크롤링하고, MySQL에 저장한 뒤  
Django 웹 서버에서 시각화 및 머신러닝 기반 예측값을 보여주는 프로젝트입니다.

---

## 📌 주요 기능

- ⏱ 10초마다 실시간 환율 크롤링 (네이버 금융)
- 🗃 MySQL DB에 자동 저장
- 📊 Matplotlib 그래프로 환율 추이 시각화
- 🔮 LinearRegression 기반 다음 환율 예측
- 🌐 Django 웹에서 실시간 표시 (자동 새로고침 포함)

---

## 🛠 기술 스택

| 구성 요소 | 기술 |
|-----------|------|
| 언어 | Python 3.11 |
| 웹 프레임워크 | Django |
| 크롤링 | Requests, BeautifulSoup |
| 머신러닝 | Scikit-learn |
| 시각화 | Matplotlib |
| DB | MySQL |
| 서버 자동화 | Git Bash, Python 스케줄링 |

---

## 🖥 실행 방법

```bash
# 1. 클론 및 가상환경 진입
git clone git@github.com:22jaegi/exchange-crawler.git
cd exchange-crawler
source venv/Scripts/activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. DB 사전 생성 (exchange_db, 테이블 포함)

# 4. 크롤링 실행 (10초 주기)
python crawler/loop_crawl.py

# 5. 모델 학습
python modeling/train.py

# 6. 웹 서버 실행
python manage.py runserver
