try:
    with open("daily_report.txt","r",encoding="utf-8")as f:
        content=f.read()
        length=len(content)
        print("報表字數統計",length)
except FileNotFoundError:
    with open("daily_report.txt","w",encoding="utf-8")as f:
        f.write("這是今天的報表")
    print("找不到 daily_report.txt，已自動建立空的報表檔案")