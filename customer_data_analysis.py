import pandas as pd
import numpy as np

df = pd.read_csv('users.csv', sep=',')

# Создание маски с True для строк, содержащих пропущенные значения
mask = df.isnull().any(axis=1)
# удаление строк, содержащих пропущенные значения
df = df[~mask]

# Удалите дубликаты
df.drop_duplicates(inplace=True)

# Замена нулей в числовых столбцах
for column in df.select_dtypes(include=np.number):
    mean = df[df[column] != 0][column].mean()
    df[column] = df[column].replace(0, mean)


