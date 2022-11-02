import re
import csv
from itertools import groupby

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  pattern = r'(^[А-Яа-я]+)(\,?\s?)([А-Яа-я]+)(\,?\s?)([А-Яа-я]*)(\,?)(\,?)(\,?)(\,?)(\,?)(\,?)([А-Яа-я]+|)(\,?)(\,?)(.[а-я]+\s\w+\s..\w+\s\w+\s\w+\s\w+.\w+\s\w+.?\w+\s?\w+\w?\s?\w+\s?\w+\s?\w\s?\w+\s?\w+\s?\w+|)(\,?\,?)(\+7|8)?\s?\(?(\d\d\d)?\)?\s?\-?(\d\d\d)?\-?(\d\d)?\-?(\d\d)?\s?\s?\,?\(?([а-я]+.\s\d\d\d\d)?\,?\)?(\,?)([A-Za-z0-9]+\.?\@?[A-Za-z]+\.?\@?[A-Za-z]+\.?\w?\w?)?'
list_base = []
for contact in contacts_list[1:9]:
    result = ','.join(contact)
    new = re.sub(pattern, r'\1,\3,\5,\12,\15,+7(\18)\19-\20-\21,\22,\24', result)
    new_element = new.split(',')
    list_base.append(new_element)

for element in list_base: # Переназначение элементов списка в случае совпадения имени и фамилии
    for element_new in list_base:
        if element[0] == element_new[0] and element[1] == element_new[1]:
            if element[2] == '':
                element[2]=element_new[2]
            if element[3] == '':
                element[3]=element_new[3]
            if element[4] == '':
                element[4]=element_new[4]
            if element[5] == '+7()--':
                element[5]=element_new[5]
            if element[6] == '':
                element[6]=element_new[6]
            if element[7] == '':
                element[7]=element_new[7]
list_base_new = [el for el, g in groupby(sorted(list_base))] # Удаление дублей

my_list = []
for element in list_base_new:
    element[6] = element[6].replace(' ', '') # Здесь я удаляю лишний пробел в доб.телефоне
    phone = element[5]+element[6] # Здесь я объединяю телефон с доб.телефоном
    string = element[0]+','+element[1]+','+element[2]+','+element[3]+','+element[4]+','+phone+','+element[7]
    my_list.append([string])

with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(my_list)

