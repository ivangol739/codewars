import requests
import json
from pprint import pprint
import os

#Астрономическая картинка дня
#Получить информация с сервера NASA

url = 'https://api.nasa.gov/planetary/apod'
params = {
  'api_key': 'gXeIRODc8aDNkfpDYecg1hZbYOMv5n9jmi1Yy3Hk',
  'date': '2024-07-18'
}
response = requests.get(url, params=params)
imageUrl = response.json()["url"]
filename = imageUrl.split('/')[-1]

#Скачать картинку
response = requests.get(imageUrl)
with open (os.path.join(os.getcwd(), "Neto", "request", filename), 'wb') as f:
  f.write(response.content)
  

#Создать папку на Яндекс диске
url_create_folder = 'https://cloud-api.yandex.net/v1/disk/resource'

params = {
  'path': 'Image',
}

headers = {
  'Authorization': '',
}

response = requests.put(url_create_folder,
                        params=params,
                        headers=headers)

#Загрузить файл на Янедкс диск
response = requests.get("https://cloud-api.yandex.net/v1/disk/resources/upload",
                        params={"path": f"Image/{filename}"},
                        headers=headers)

url_upload = response.json()["href"]

with open(filename, 'rb') as f:
  requests.put(url_upload, files={'file': f})