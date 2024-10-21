numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
numbers_bez_govna = [2, -93, -2, 8,-44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
churka = sum(numbers_bez_govna) / len(numbers)
numbers_cucumber = [2, -93, -2, 8,churka,-44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
xach = sum(numbers_cucumber) / len(numbers_cucumber)

print("Измененный список:",numbers_cucumber )
