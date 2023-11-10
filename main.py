import random

def guess_the_number(x1, x2, n):
    target_number = random.randint(x1, x2)
    attempts = 0

    print(f"猜一個在 {x1} 和 {x2} 之間的數字！")

    while True:
        guess = int(input("你的猜測："))
        attempts += 1

        if guess == target_number:
            print(f"恭喜！你猜對了，目標數字是 {target_number}。你總共猜了 {attempts} 次。")
            break
        elif guess < target_number:
            print("太低了，再試一次！")
        else:
            print("太高了，再試一次！")

        if attempts == n:
            print(f"抱歉，你已經猜了 {n} 次，仍未猜對。正確的數字是 {target_number}。")
            break

if __name__ == "__main__":
    x1 = int(input("請輸入x1的值："))
    x2 = int(input("請輸入x2的值："))
    n = int(input("請輸入n的值："))

    guess_the_number(x1, x2, n)