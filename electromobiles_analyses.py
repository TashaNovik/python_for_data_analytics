import pandas as pd
Cars = pd.read_csv('Electric_Car.csv')
# Cars - it is dataframe
print(Cars.dtypes)
# todo: Сагрегируйте данные по брендам (поле Brand).
# todo: Вычислите среднее значение цены (поле PriceEuro) для каждой группы.
# todo: Сохраните результаты проделанных действий в датафрейм с именем Carsgroupby

Carsgroupby = Cars.groupby('Brand')['PriceEuro'].mean()
# в этом случае результатом будет Series, а не DataFrame
# преобразуйте его в DataFrame, если нужно
Carsgroupby = Carsgroupby.to_frame(name='PriceEuro') # столбец будет называться 'PriceEuro'

