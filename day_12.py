import random
import string

pwd=''.join(random.choices(string.ascii_letters + string.digits, k=9))

print("隨機密碼:",pwd)