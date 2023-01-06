num = 0

while True:
    number = input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ')
    if not number.isnumeric():
        print('정수를 입력하세요')
    elif number == "1" or number == "2" or number == "3":
        break
    else:
        print('1,2,3 중 하나를 입력하세요')

number = int(number)
while num < number:
    num+=1
    print(num)