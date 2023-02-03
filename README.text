# gemstone-store

клонировать проект из гит git clone git@github.com:varias070/gemstone-store.git
перейти в дерикторию проекта cd gemstone-store
выполнить: 
  docker-compose build
  docker-compose up
  
точка доступа для загрузки файла http://127.0.0.1:8001/add_deal
запрос для загрузки csv 

import requests

headers = {
        "Content-Type": "text/csv"
}
url = "http://127.0.0.1:8001/add_deal"
file = "deals.csv"
with open(file, "rb") as f:
    r = requests.post(url, data=f, headers=headers)
    print(r.status_code)

точка доступа для выполнение запроса в базу данных http://127.0.0.1:8001/find_top_five_clients
запрос для выполнение поиска 

import requests


url = 'http://127.0.0.1:8001/find_top_five_clients'
r = requests.get(url)
print(r.json())
