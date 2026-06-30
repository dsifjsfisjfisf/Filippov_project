#Найдите ключ с минимальным значением
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}
min_key = min(sample_dict, key=sample_dict.get)
print(min_key)
