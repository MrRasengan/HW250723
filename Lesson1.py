# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите общее колличество монеток: "))
sp = []
for _ in range(n):
    sp.append(int(input("Монетки перевёрнутые вверх гербом: ")))
gerb = 0
reshk = 0
for i in sp:
    if i > 0:
        reshk = reshk + 1
        if gerb < reshk:
            gerb = reshk
    else:
        reshk = 0
print(gerb)