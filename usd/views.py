from django.shortcuts import render
from django.db import connection
import matplotlib.pyplot as plt
import io, base64
import joblib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import platform

if platform.system() == "Windows":
    matplotlib.rc("font", family="Malgun Gothic")  # 윈도우용
else:
    matplotlib.rc("font", family="AppleGothic")  # mac용 등

matplotlib.rcParams["axes.unicode_minus"] = False  # 음수 기호 깨짐 방지


def usd_graph(request):
    # DB에서 최근 20개 환율 데이터 가져오기
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, datetime, usd_rate FROM usd_exchange ORDER BY id DESC LIMIT 20"
        )
        rows = cursor.fetchall()[::-1]

    # 데이터 분리
    ids = [r[0] for r in rows]
    datetimes = [r[1].strftime("%H:%M:%S") for r in rows]
    rates = [r[2] for r in rows]

    # 그래프 그리기
    plt.figure(figsize=(8, 4))
    plt.plot(datetimes, rates, marker="o")
    plt.xticks(rotation=45)
    plt.title("USD 환율 추이")
    plt.tight_layout()

    # 이미지 → base64 인코딩
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    graph = base64.b64encode(buf.read()).decode()
    buf.close()

    # 모델 예측
    model = joblib.load("modeling/model.pkl")
    next_id = ids[-1] + 1
    predicted = model.predict([[next_id]])[0]

    return render(
        request, "usd.html", {"graph": graph, "prediction": round(predicted, 2)}
    )
