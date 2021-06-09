# 5.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
#  例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制
n = int(input("Input number:"))
a = int(input("Input a:"))
temp = 0
s = 0
for _ in range(1, n + 1):
    temp = temp * 10 + a
    s += temp
print(f"s={s}")
