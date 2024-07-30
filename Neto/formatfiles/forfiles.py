import csv
import os
import json
import pprint


file1 = os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "newsafr.csv",)
file2 = os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "newsafr.json")
file3 = os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "newsafr.xml")

#ЧТЕНИЕ CSV ФАЙЛА ПОСТРОЧНО ЛЮБОЙ ДЛИНЫ
with open(file1, newline="", encoding="UTF-8") as f:
  reader = csv.reader(f)
  count = -1
  for row in reader:
    if count >= 0:
      print(row[-1])
    count += 1

#ЧТЕНИЕ ФАЙЛА ЦЕЛИКОМ
with open(file1, newline="", encoding="UTF-8") as f:
  reader = csv.reader(f)
  new_list = list(reader)
  
#Убрать заголовок
header = new_list.pop(0)
  
#ЗАПИСЬ ФАЙЛА
csv.register_dialect("comma_no_quoting", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
csv.register_dialect("semicolon_quote_all", delimiter=";", quoting=csv.QUOTE_ALL)

with open(os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "result.csv"), "w", encoding="UTF-8", newline="") as f:
  writer = csv.writer(f, dialect="semicolon_quote_all")
  writer.writerow(header)
  writer.writerows(new_list[:3])
  
  
#Чтение файла в словарь
with open(file1, newline="", encoding="UTF-8") as f:
  reader = csv.DictReader(f)
  for row in reader:
    print(row["title"])



#ЧТЕНИЕ JSON 
with open(file2, encoding="UTF-8") as f:
  json_data = json.load(f)
  
new_list = json_data["rss"]["channel"]["items"]

for row in new_list:
  print(row["title"])
  
#ЗАПИСЬ JSON
with open(os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "resultJSON.json"), "w", encoding="UTF-8", newline="") as f:
  json.dump(new_list, f, ensure_ascii=False, indent=4)



#СОЗДАЕМ ПАРСЕР И ЧИТАЕМ XML
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="UTF-8")
tree = ET.parse(file3, parser)


root = tree.getroot()
print(root.tag)
print(root.attrib)

new_list = root.findall("channel/item")
for item in new_list:
  title = item.find("title")
  print(title.text)
  
#ЗАПИСЬ XML
tree.write(os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "resultXML.xml"), encoding="UTF-8")

#дгугой пример
xml_str = '<root><channel type="dict"><title type="str">Дайджест новостей о python</title><link type="str">https://pythondigest.ru/</link></channel></root>'
root = ET.fromstring(xml_str)
tree = ET.ElementTree(root)
tree.write("files/result2.xml", encoding="utf-8")
  