import pandas as pd
import os

def save_to_csv(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
    print(f"داده در {path} ذخیره شد")

