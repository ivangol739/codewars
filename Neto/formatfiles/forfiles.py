import csv
import os
import json
import pprint


file1 = os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "newsafr.csv",)
file2 = os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "newsafr.json")


##ЧТЕНИЕ CSV ФАЙЛА ПОСТРОЧНО ЛЮБОЙ ДЛИНЫ
# with open(file1, newline="", encoding="UTF-8") as f:
#   reader = csv.reader(f)
#   count = -1
#   for row in reader:
#     if count >= 0:
#       print(row[-1])
#     count += 1

##ЧТЕНИЕ ФАЙЛА ЦЕЛИКОМ
# with open(file1, newline="", encoding="UTF-8") as f:
#   reader = csv.reader(f)
#   new_list = list(reader)
  
#Убрать заголовок
# header = new_list.pop(0)
  
#ЗАПИСЬ ФАЙЛА
# csv.register_dialect("comma_no_quoting", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")
# csv.register_dialect("semicolon_quote_all", delimiter=";", quoting=csv.QUOTE_ALL)

# with open(os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "result.csv"), "w", encoding="UTF-8", newline="") as f:
#   writer = csv.writer(f, dialect="semicolon_quote_all")
#   writer.writerow(header)
#   writer.writerows(new_list[:3])
  
  
##Чтение файла в словарь
# with open(file1, newline="", encoding="UTF-8") as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     print(row["title"])



##ЧТЕНИЕ JSON 
# with open(file2, encoding="UTF-8") as f:
#   json_data = json.load(f)
  
# new_list = json_data["rss"]["channel"]["items"]

# for row in new_list:
#   print(row["title"])
  
##ЗАПИСЬ JSON
# with open(os.path.join(os.getcwd(), "Neto", "formatfiles", "fileslections", "resultJSON.json"), "w", encoding="UTF-8", newline="") as f:
#   json.dump(new_list, f, ensure_ascii=False, indent=4)

  
  