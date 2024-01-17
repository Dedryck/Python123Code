Balance = 1000
choice = int(input())

if choice == 1:
    money = int(input())
    if money < 100 or money % 100 != 0:
        print("Incorrect Amount")
    else:
        Balance -= money
        if Balance > 0:
            print(f"Balance:{Balance}")
        else:
            print("Insufficient Funds")
elif choice == 2:#注意这里需要捕捉一个异常浮点数据
    try:
        money = int(input())
        if money < 100 or money % 100 != 0:
            print("Incorrect Amount")
        else:
            Balance += money
            print(f"Balance:{Balance}")
    except ValueError:
        print("Incorrect Amount")
else:
    print("Wrong Option")