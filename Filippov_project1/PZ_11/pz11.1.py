# 1. Даны значения роста 20 юношей. Определить сколько юношей будут направлены
# в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).

import random

heights = [random.randint(140, 200) for _ in range(20)]

print("Рост юношей:", heights)

basketball = len(list(filter(lambda h: h >= 190, heights)))
football = len(list(filter(lambda h: h < 190, heights)))

print("В баскетбольную команду (рост от 190):", basketball)
print("В футбольную команду (остальные):", football)
