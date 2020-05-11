num = 56
user_num = 0
cnt = 0

while True:
    user_num = int(input("Привіт, я загадав число від 1 до 100, відгадай його: "))
    cnt += 1
    if user_num == num:
        print(f'Вітаю, ви відгадали число за {cnt} спроб!')
        break
    elif user_num > num:
        print('Число менше від того що ви написали!')
    else:
        print('Число більше від того що ви написали')

