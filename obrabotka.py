# Aku

import pandas as pd #импортируем pandas
import numpy as np  #импортируем numpy
df = pd.read_csv("var2.csv") #читаем датасет и записываем в переменную df

    
    #Попробуем найти и по возможности удалить колонки, в которых есть всего одно значение во всех строчках 
'''def  delete (self):
    df = df[[c for c
    in list(df)
    if len(df[c].unique()) > 1]] #Перезаписываем датасет, оставляя только те колонки, 
                                        # в которых больше одного уникального значения'''

df.drop_duplicates(inplace=True) #Делаем это, если считаем нужным: удаление строк, которые содержат одну и 
                                # ту же информацию в одном и том же порядке, что и уже одна из существующих строчек

df = df.groupby(df.columns.tolist()).size().reset_index(name='Size')            


df.info()