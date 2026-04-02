import pandas as pd

# CSV 読み込み
df = pd.read_csv("kinjiro.csv", encoding="utf-8")

# 全体の列数と最初の5行
print(df.head())
print(df.columns)

print("\n--- 出勤・退勤・休憩・休暇・遅刻・早退 に関係する列 ---")

# 必要な列抽出
keywords = ["出勤", "退勤", "休憩", "休暇", "遅刻", "早退"]

for col in df.columns:
    if any(key in col for key in keywords):
        print(col)