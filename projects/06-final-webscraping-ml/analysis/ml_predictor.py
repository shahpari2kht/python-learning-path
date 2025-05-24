import pandas as pd
from sklearn.tree import DecisionTreeRegressor

def predict_covid_deaths(csv_path):
    """
    Predicts deaths based on cases using simple Decision Tree (demo).
    """
    try:
        df = pd.read_csv(csv_path)
        if 'cases' not in df or 'deaths' not in df:
            print("ستون موردنیاز پیدا نشد")
            return
        X = pd.to_numeric(df['cases'], errors='coerce').fillna(0).values.reshape(-1, 1)
        y = pd.to_numeric(df['deaths'], errors='coerce').fillna(0).values
        if len(X) < 2:
            print("داده کافی نیست")
            return
        model = DecisionTreeRegressor()
        model.fit(X, y)
        pred = model.predict([[1000000]])
        print(f"پیش‌بینی تعداد فوتی‌ها برای ۱ میلیون مبتلا: {int(pred[0])}")
    except Exception as e:
        print("خطا در تحلیل:", e)

