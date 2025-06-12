import joblib
import numpy as np

model = joblib.load("modeling/model.pkl")
next_id = 1000  # 예시용. DB에서 max(id)+1로 자동화 가능
pred = model.predict([[next_id]])
print(f"🔮 예측 환율: {pred[0]:.2f} 원")
