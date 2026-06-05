#В исходном текстовом файле найти все годы деятельности писателя (например, 1821 года, 1837 год, 1843 году и так далее по всему тексту), Посчитать кол-во полученных элементов.
import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as f:
    text = f.read()

years = re.findall(r'\b\d{4}\s+(?:года|год|году)\b', text)

print(*list(map(lambda x: x, years)), sep='\n')
print(f"\nКоличество: {len(years)}")
