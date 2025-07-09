numbers = input("請輸入數字，用空白分隔:")
total= sum(int(x)for x in numbers.split())
print("總合為",total)