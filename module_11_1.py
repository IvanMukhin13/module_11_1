from PIL import Image
import numpy as np
import pandas as pd

img = Image.open('Dino_Crisis_logo.png')
print(img.size) # (1400, 788)
img = img.resize((100, 100)) # (100, 100)
print(img.size)
img.show()


first = np.array([[1, 2, 3, 4, 5]])
second = np.array([[6, 7, 8, 9, 0]])
print(first.min())
print(second.min())
print(second.max())
print(first.max())
print(first.mean())
print(second.mean())
print(first + second)

data_base = pd.DataFrame({
    '№': [1, 2, 3, 4, 5],
    'Name': ['Ivan', 'Aleksey', 'Nikita', 'Oleg', 'Artem'],
    'Height': [189, 195, 205, 183, 191],
    'Weight': [85, 88, 96, 76, 87]
})

print('-----Вся база-----')
print(data_base)
print()
print('-----Показать первые значения-----')
print(data_base.head(2))  # показать первые значения
print()
print('-----Показать последние значения-----')
print(data_base.tail(2))
print()
print('-----Какое количество строк и столбцов-----')
print(data_base.shape)
print()
print('-----Индексы-----')
print(data_base.index)
print()
print('-----Название столбцов-----')
print(data_base.columns)
print()
print('-----Поменять строки и столбцы местами-----')
print(data_base.T)
print()
print(data_base.info)
print('-----Данные-----')
print(data_base.loc[0])
print()