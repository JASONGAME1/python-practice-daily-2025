answer = 57
while True:
    guess = int(input("請輸入數字"))
    if guess == answer:
        print("猜對囉")
        break
    else:    
        print("請繼續猜")