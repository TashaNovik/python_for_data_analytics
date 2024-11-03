import pandas as pd
Cars = pd.read_csv('Electric_Car.csv')
#todo: Сделайте срез по столбцу PriceEuro со значениями более 50000 и по столбцу TopSpeed_KmH со значениями более 200.
# todo: Переназначьте индексы таблицы начиная с нуля.
# todo: Сохраните результаты проделанных действий в датафрейм с именем Cars_speed
Cars_speed = Cars.loc[(Cars.PriceEuro > 50000) & (Cars.TopSpeed_KmH > 200)].copy()
Cars_speed = Cars_speed.reset_index(0, drop=True)


