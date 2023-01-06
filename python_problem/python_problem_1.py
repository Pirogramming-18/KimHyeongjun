import random

def brGame():
    num = 0
    num_sum = 0

    while True:
        com_number = random.randint(1, 3)
        num_sum += com_number
        while num < num_sum:
            num+=1
            print('computer', num)
            if num == 31:
                print('player win!')
                return
            
        while True:
            number = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
            if not number.isnumeric():
                print('정수를 입력하세요')
            elif number == "1" or number == "2" or number == "3":
                break
            else:
                print('1,2,3 중 하나를 입력하세요')

        num_sum += int(number)

        while num < num_sum:
            num+=1
            print("player", num)
            if num == 31:
                print('computer win!')
                return

brGame()

    