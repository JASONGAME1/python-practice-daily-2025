import os 
from datetime import datetime

today = datetime.today().strftime("%Y%m%d")
folder_name="報表_"+today
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print("已建立資料夾:",folder_name)
else:
    print("資料夾已存在",folder_name)