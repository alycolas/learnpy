def zip(num):
    while num != 1:
        if num % 2 != 0:
            num = num * 3 + 1
        else:
            num = num // 2
        print(num)
