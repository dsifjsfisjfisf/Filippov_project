# 1. Даны значения роста 20 юношей. Определить сколько юношей будут направлены в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).

import random

heights = []
for i in range(20):
    height = random.randint(140, 200)
    heights.append(height)
    print(f"Рост {i+1}-го юноши: {height}")

basketball = 0
football = 0

for h in heights:
    if h >= 190:
        basketball += 1
    else:
        football += 1

print("\nВ баскетбольную команду (рост от 190):", basketball)
print("В футбольную команду (остальные):", football)
