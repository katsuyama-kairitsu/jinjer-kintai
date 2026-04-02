import pandas as pd

# 勤次郎CSVの読み込み
kinjiro = pd.read_csv("kinjiro.csv", encoding="utf-8")

# Jinjerテンプレの列構造（必要な列だけ）
jinjer_columns = [
    "名前", "従業員ID", "年月日", "打刻グループID",
    "出勤予定時刻", "退勤予定時刻", "休憩予定時刻", "復帰予定時刻",
    "休日",
    "出勤", "退勤", "休憩", "復帰"
]

# 空のテンプレを作成
jinjer = pd.DataFrame(columns=jinjer_columns)

# 勤次郎 → Jinjer のマッピング
jinjer["従業員ID"] = kinjiro["個人  CD"]
jinjer["年月日"] = kinjiro["年月日"]

# 予定
jinjer["出勤予定時刻"] = kinjiro["予定出勤時刻"]
jinjer["退勤予定時刻"] = kinjiro["予定退勤時刻"]
jinjer["休憩予定時刻"] = kinjiro["予定休憩①開始時刻"]
jinjer["復帰予定時刻"] = kinjiro["予定休憩①終了時刻"]

# 休日コード
jinjer["休日"] = kinjiro["出勤日区分"]

# 実績
jinjer["出勤"] = kinjiro["実出勤時刻"]
jinjer["退勤"] = kinjiro["実退勤時刻"]
jinjer["休憩"] = kinjiro["休憩開始時刻"]
jinjer["復帰"] = kinjiro["休憩終了時刻"]

# 必要なら固定値を入れる（例：打刻グループID）
jinjer["打刻グループID"] = "1"  # ←会社の設定に合わせて変更

# CSVとして保存
jinjer.to_csv("jinjer_upload.csv", index=False, encoding="utf-8-sig")

print("変換完了：jinjer_upload.csv を確認してください")