# 4.输入两个正整数m和n，设计函数求其最大公约数(greatest common divisor)和最小公倍数(lowest common multiple )
# 最大公约数：指两个或多个整数共有约数中最大的一个
# 最小公倍数：两个或多个整数公有的倍数叫做它们的公倍数，其中除0以外最小的一个公倍数就叫做这几个整数的最小公倍数


def gcd(m, n):
    while n != 0:
        temp = m % n
        m = n
        n = temp
    return m


def lcm(m, n):
    return m * n // gcd(m, n)


def main():
    m = int(input("input m:"))
    n = int(input("input n:"))
    print(f"最大公约数：{gcd(m, n)}")
    print(f"最小公倍数：{lcm(m, n)}")


if __name__ == '__main__':
    main()
