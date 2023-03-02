# -*- coding: utf-8 -*-
"""Seletor de pets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17KHyEPnSJhDQyMPYKOmgJJ6IbIwv1-7u
"""

# base https://cataas.com/#/
# apiUsada https://cataas.com/api/cats?tags=cute
# base https://dog.ceo/dog-api/documentation/
# apiUsada https://dog.ceo/api/breeds/list/all
import requests
import json

select_pet = 0

while select_pet > 1 or select_pet <3:
  select_pet = int(input("Selecione um pet\n 1-Gatos \n 2-Cachorros\n 3-Outro Pet\n"))
  if select_pet == 1:
    cats_data_base = requests.get("https://cataas.com/api/cats?tags=cute")
    cats = json.loads(cats_data_base.text)
    print("Características de gatos\n",cats[0]['tags'])

  if select_pet ==2:
    dogs_data_base = requests.get("https://dog.ceo/api/breeds/list/all")
    dogs = json.loads(dogs_data_base.text)
    print("Raça dos Cachorros\n",dogs['message'])
  
  if select_pet ==3:
    print("No momento só temos cães e gatos!\n ---------Aguarde novas atualizações!!!------------\n")