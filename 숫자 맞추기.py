import random

def guess_number():
    number = random.randint(1, 100)
    print("1부터 100까지")

    while True:
        try:
            guess = int(input("예상 값: "))
            if guess < number:
                print("낮음!")
            elif guess > number:
                print("높음!")
            else:
                print("정답!")
                break
        except ValueError:
            print("잘못된 값 입력.")

guess_number()
