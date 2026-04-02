import pandas as pd

# 勤次郎CSVの読み込み
kinjiro = pd.read_csv("kinjiro.csv", encoding="shift_jis")

# Jinjer用のデータフレーム作成
jinjer = pd.DataFrame()

# 基本情報
jinjer["名前"] = kinjiro["個人 名"]
jinjer["従業員ID"] = kinjiro["個人 CD"]
jinjer["年月日"] = pd.to_datetime(kinjiro["年月日"]).dt.strftime("%Y/%m/%d")
jinjer["打刻グループID"] = "" #打刻グループを付ける？
# 予定（スケジュール）
jinjer["出勤予定時刻"] = kinjiro["予定出勤時刻"]
jinjer["退勤予定時刻"] = kinjiro["予定退勤時刻"]
jinjer["休憩予定時刻"] = kinjiro["予定休憩①開始時刻"]
jinjer["復帰予定時刻"] = kinjiro["予定休憩①終了時刻"]

# 実績（打刻）
jinjer["出勤"] = kinjiro["実出勤時刻"]
jinjer["退勤"] = kinjiro["実退勤時刻"]
jinjer["休憩"] = kinjiro["予定休憩①開始時刻"]  # 必要に応じて変更
jinjer["復帰"] = kinjiro["予定休憩①終了時刻"]

# 休暇（必要な場合）
# 例：時間年休が1以上なら「年次有給」として登録
jinjer["休日休暇名1"] = kinjiro["時間年休休暇"].apply(
    lambda x: "年次有給" if x > 0 else ""
)

# 時間休の開始・終了（必要な場合）
jinjer["開始時間"] = kinjiro.get("時間年休出勤前", "")
jinjer["終了時間"] = kinjiro.get("時間年休退勤後", "")

# CSV出力
jinjer.to_csv("jinjer_upload.csv", index=False, encoding="utf-8-sig")

print("Jinjer用CSVを出力しました。")