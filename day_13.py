from datetime import datetime
today= datetime.today().strftime("%Y%m%d")
filename = today + "_report.txt"
print("今天的報表檔名為:", filename)