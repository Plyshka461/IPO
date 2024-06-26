import pandas as pd

# Считываем данные из файла
df = pd.read_csv("employees.csv")

# Устанавливаем индексы (например, используем столбец "ФИО")
df.set_index("ФИО", inplace=True)

# Выводим данные в виде таблицы
print(df)
