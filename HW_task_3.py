# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать “больше” или “меньше” после каждой попытки. 

from random import randint

LIMIT_1 = 0
LIMIT_2 = 1000

num = randint(LIMIT_1, LIMIT_2)
flag = False
for i in range(10):
    user_num = int(input(f"Попытка угадать № {i+1}. Введите число от {LIMIT_1} до {LIMIT_2}: "))
    if user_num == num:
        print("Угадали!")
        flag = True
        break
    else:
        if user_num < num:
            print(f"Загаданное число больше {user_num}")
        else:
            print(f"Загаданное число меньше {user_num}")
if not flag:
    print(f"Вы проиграли. Загаданное число было {num}")