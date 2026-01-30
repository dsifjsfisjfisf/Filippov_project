#
magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}

print("1. Товары из магнита, отсутсвующие в пятерочке", magnit - pyaterochka)
print("2. Товары из Пятерочки, отсутсвующие в магните", pyaterochka - magnit)
print("3. Полный перечень всех товаров", magnit | pyaterochka)
print("4. Перечни товаров равны", magnit == pyaterochka)
