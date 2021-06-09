
# 2.有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？（输出前40个月即可）
def rabbit(month):
    if month<2:
        return 1
    return rabbit(month-1)+rabbit(month-2)

if __name__=='__main__':
    # n=int(input("input month:"))
    n=40
    for i in range(2,n+1):
        print(f"前{i}个月兔子总数:{rabbit(i)}")

