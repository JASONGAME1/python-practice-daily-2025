pwd= input("請輸入密碼")
if len(pwd)>=9 and any(char.isdigit() for char in pwd):
    print("密碼強度合格")
else:
    print("密碼強度不合格")