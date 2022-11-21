# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:36:01 2022

@author: Маша
"""

import numpy as np

a= np.array([[8,2,6],
            [9, 6,2]])
b= np.array([[4, 6],
             [5, 2],
             [1, 8]])
c= np.array ([[3],[7]])
d= np.array([[8], [7], [9]])

bmultc=np.dot(b,c)
print('b умножить на вектор с:',bmultc, end='\n')

bmultctrans=bmultc.T
print('транспонируем предыдущее',bmultctrans, end='\n')

multd=np.dot(bmultctrans, d)
print('умножаем на вектор д',multd, end='\n')

norma=np.linalg.norm(a)
print("норма а",norma, end='\n')

result=multd+norma
print("результат:",result, end='\n')