content= input("請輸入報表內容:")
with open ("daily_report.txt","w",encoding="utf-8")as f:
    f.write(content)
print("已儲存daily_report.txt!")