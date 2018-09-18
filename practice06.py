# 練習題 6:
# 寫一個函式，使用者輸入一個長數字，透過函式計算幾位數，
# 要列印出函式回傳的值。例如 傳入 23323456 要回傳 8
print("test6")

def test6 (m):
    a = m%1;
    if a >= 0 :
        print(len(str(m)))
    else:
        print("erro")

num = int(input("num: "))
test6(num)