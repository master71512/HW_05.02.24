# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LIMIT_1 = 2
LIMIT_2 = 100000

while True:
    num = int(input(f"Введите число от {LIMIT_1} до {LIMIT_2}: "))
    if LIMIT_1 <= num <= LIMIT_2:
        break

flag = False

if num == 2 or num == 3:
    print(f"Число {num} простое")
elif num % 2 == 0:
    print(f"Число {num} составное")
else:
    for i in range(3, int(num**0.5)+2, 2):
        if num % i == 0:
            print(f"Число {num} составное")
            break
        else:
            flag = True
if flag:
    print(f"Число {num} простое")
        
