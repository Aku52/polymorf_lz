# Aku

import pandas as pd

class Processing:

    def __init__(self):
        pass

    # Oбработка и фильтрация данных файла
    def __invert__(self):
       
        # Читаем файл
        df = pd.read_csv('var2.csv')
        
        # Разделение датасета 
        filtered1_df = df[df['Тип операции'] == 'списание средств']
        filtered2_df = df[df['Тип операции'] != 'списание средств']
        
        # Создание отдельных файлов 
        filtered1_df.to_csv('sredstva_1.csv', index= False, encoding='utf-8')
        filtered2_df.to_csv('sredstva_2.csv', index= False, encoding='utf-8')
        
        # Создание полиморфизма унарного оператора для удаления дубликатов
        num_duplicates = df.duplicated().sum()
        df = df.drop_duplicates()
        # Bывод количества удаленных дубликатов
        print('Количество повторяющихся строк в наборе:', num_duplicates)


def main():
    pay = Processing()
    ~pay


if __name__ == "__main__":
    main()





    