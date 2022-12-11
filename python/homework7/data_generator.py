import xml.etree.ElementTree as ETree
from random import randint as r


def generate_data():
    limit = 125
    data = []
    for i in range(limit):
        day = str(r(1, 30))
        if len(day) == 1:
            day = f'0{day}'
        month = str(r(1, 12))
        if len(month) == 1:
            month = f'0{month}'
        phones = ''
        for j in range(0, r(1, 2)):
            phone = f'7{r(901, 999)}{r(100, 999)}{r(0, 9)}{r(0, 9)}{r(0, 9)}{r(0, 9)}'
            if j != 0:
                phones += ', '
            phones += phone
        user = {
            'id': i,
            'last_name': f'Фамилия {i + 1}',
            'name': f'Имя {i + 1}',
            'b_date': f'{day}.{month}.{r(1971, 2020)}',
            'job': f'место работы {i + 1}',
            'phone': phones
        }
        data.append(user)
    return data


def data_from_xml(filename):
    data = []
    tree = ETree.parse(filename)
    phonebook = tree.getroot()

    for item in phonebook:
        user = {}
        for i in item:
            user[i.tag] = i.text
        data.append(user)
    return data
