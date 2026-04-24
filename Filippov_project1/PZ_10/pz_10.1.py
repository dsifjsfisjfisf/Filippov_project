# 2. Из предложенного текстового файла (text18-24.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв.
# Сформировать новый файл, в который поместить текст в стихотворной форме
# предварительно заменив символы нижнего регистра на верхний.

with open('text18-24.txt', 'r', encoding='utf-16le') as f:
    content = f.read()

print("Содержимое файла:")
print(content)

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
letter_count = 0
for char in content:
    if char in letters:
        letter_count += 1

print("\nКоличество символов, принадлежащих к группе букв:", letter_count)

with open('poetic.txt', 'w', encoding='utf-16le') as f:
    f.write(content.upper())

print("\nФайл poetic.txt создан")
