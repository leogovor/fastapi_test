import pandas as pd

# Чтение таблиц из файлов .xlsx
table1 = pd.read_excel('table1.xlsx')  # Замените 'table1.xlsx' на путь к вашему файлу
table2 = pd.read_excel('table2.xlsx')  # Замените 'table2.xlsx' на путь к вашему файлу
key_table = pd.read_excel('key_table.xlsx')  # Замените 'key_table.xlsx' на путь к вашему файлу

# Объединение таблиц
merged_table = key_table.merge(table1, left_on='table1_id', right_on='id', how='left') \
                         .merge(table2, left_on='table2_id', right_on='id', how='left')

# Результат
print(merged_table)