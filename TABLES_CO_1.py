import pandas as pd
import pyexcel as pxl


# Чтение таблиц из файлов .xlsx
table1 = pd.read_excel('/Documents/table1.xlsx')
table2 = pd.read_excel('/Documents/table2.xlsx')  
key_table = pd.read_excel('/Documents/key_table.xlsx')

# Объединение таблиц
merged_table = key_table.merge(table1, left_on='table1_id', right_on='id', how='left') \
                         .merge(table2, left_on='table2_id', right_on='id', how='left')

# Результат
print(merged_table)
with open("/Documents/merged_table.xlsx", "w") as file:
    file.write(merged_table)

'''
    ## Импорт данных
df = pd.read_csv('file') – импорт файла
df = pd.read_csv('file', sep=",") – импорт файла с разделителем «запятая»

# Экспорт данных
save_file.to_csv('file.csv', encoding='utf8') – сохранение датафрейма в csv-файл с кодировкой utf8

# Вывод на экран
df – вывести весь датафрейм
df.info – информация о датафрейме
df.head(5) – первые пять строчек
df.tail(5) – последние пять строчек
df.sample(5) – случайные пять строчек
df.shape – количество строк и столбцов
df.dtypes – типы данных в столбцах
df.columns – названия столбцов
f['col1'] – значения столбца col1
df['col1'][0:20] – срез столбца col1
df[['col1', 'col2']] – значения нескольких столбцов
df.loc['index_name'] – строки и/или столбцы по нечисловому значению индекса
df.iloc[0] – строки и/или столбцы по числовому индексу
df.iloc[2,4] – значение ячейки в третьей строчке и пятом столбце

# Объединение датафреймов
df1 = pd.concat([df1, df2], axis=0) – к df1 добавляем строчки df2
df1 = pd.concat([df1, df2], axis=1) – к df1 добавляем столбцы df2
df1 = df1.append(df2) – к df1 добавляем строчки df2

# Копирование датафрейма
df2 = df1.copy – создает глубокую копию датафрейма

# Добавление строчек и столбцов
new_row = {'col1': 'Hello', 'col2': 123}
df = df.append(new_row, ignore_index=True) – добавляет в конец df строчку new_row
df.loc[2] = ['Hello', 123] – добвляет строчку на третье место с начала фрейма
df['new_column'] = 'abcd' – создает столбец со значениями abcd

# Удаление строчек и столбцов
df.drop(26954, 0) – удаляет строчку номер 26954
df.drop('col', 1) – удаляет столбец col

# Переименование столбцов
df.rename(columns={'col1': 'new_col1'}) – меняет имя столбца с col1 на new_col1

# Изменение значения в ячейке
df['col'] = df['col'].replace(to_replace=2020, value=2021) – меняем все значения с 2020 на 2021
df['col'] = df['col'].mask(df['col'] == 2001, 2021) – аналогично, меняем все значения с 2020 на 2021

# Сортировка
df.sort_values('col', ascending=False) – сортировка в обратном алфавитном порядке
df.sort_values(['col1', 'col2']) – сортировка по двум столбцам. col1 – в приоритете, так как первый

# Изменение типов
df['col'] = df['col'].astype(str) – меняет тип переменных на str
df['col'] = df['col'].astype(float) – на float
df['col'] = df['col'].astype('int32') – на int32
df['col'] = df['col'].astype('int64') – на int64
df['col'] = pd.to_numeric(df['col1']) –  на int64

# Удаление и замена NaN-значений
df.dropna() – удаляет строчки с отсутствующими значениями
df.dropna(axis=1) – удаляет столбцы с отсутствующими значениями
df.fillna('abcd') – меняет NaN на abcd

# Удаление лишних пробелов
df['col'] = df['col'].map(str.strip) – удаляет пробелы слева и справа

# Обработка дат
df['col'] = pd.to_datetime(df['col']) – меняет тип на datetime64[ns]
df['col'].dt.day – вытаскивает из столбца col только значение дня
df['col'].dt.month – только месяц
df['col'].dt.year – только год

# Фильтрация и поиск
df['col'].str.startswith('a') – ищет совпадение по первому символу строки, не поддерживает regex
df['col'].str.endswith('a') – ищет совпадение по последнему символу строки, не поддерживает regex
df['col'].str.match('a') – определяет, начинается ли каждая строка с шаблона
df['col'].str.findall('a') – возвращает совпадения шаблонов
df['col'].str.contains('a') – в результате поиска возвращает булево значение
df['col'].str.extractall('a') – вернет столбец с поисковым шаблоном
df.loc[df['col'].isin(['a', 'b'])] – ищет совпадения в столбцах

# Статистические данные
df.describe() – статистическая сводка по численным значениями

# Подсчет количества повторов
df['col'].value_counts() – показывает сколько раз значения повторяются в столбце
df['col_result'] = df.groupby('col')['col'].transform('count') – создает столбец с количеством повторов значений
'''