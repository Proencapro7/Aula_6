# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-Jwq98fcVt1dL6112S7xY0JJ6NxY7Vf7
"""

# import random
# aleatorio = random.randint(1,10)
# print(aleatorio)






# if chute_aleatorio ==2:
#     print('acertei', chute_aleatorio)
# else:
#   print('errei', chute_aleatorio)


import random

aleatorio =  random.randint(10000,200000)
Senha = int(input('Digite Senha:'))

#condição verdadeira
if Senha <= aleatorio:
   print(aleatorio + Senha)
   print('Acesso liberado', aleatorio)
# codição falsa
else:
    print('senha incorreta', aleatorio)



