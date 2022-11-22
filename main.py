import requests
import string


############################################## 1 задание, упражнение 1 #############################################
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
#Функция для тестирования
def geo_(my_list: list)->list:
    my_dict = [{k:v for (k,v) in element.items() if v[1]=='Россия'} for element in geo_logs]
    return list(filter(None,my_dict))

############################################## 1 задание, упражнение 2 #############################################

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
#Функция для тестирования
def ids_(my_dict: dict)->list:
    my_list = []
    for values in ids.values():
        my_list.extend(values)
    new_list = set(my_list)
    return list(new_list)

############################################# 1 задание, упражнение 3 #############################################
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
#Функция для тестирования
def queries_(queries: list) -> list:
    len_queries = len(queries)
    my_list = [round(len(element.split(' '))/len_queries*100, 2) for element in queries]
    return my_list


########################### 2 Задание ##################################
class YaDisk:
    def __init__(self, tokenYa):
        self.token = tokenYa

    def get_headers(self):
        '''
        Даный метод возращается heders, используется в других методах при формировании запроса
        '''
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def category_created(self, path_to_file: str):
        '''
        Данный метод создает каталог на Яндекс.диске. На вход получает название каталога
        '''
        digit = string.digits
        character = string.ascii_lowercase
        if len(path_to_file)>4:
            return "len name of folder > 4"
        if any(d in digit for d in path_to_file):
            return 'digit'
        if any(letter in character for letter in path_to_file):
            return 'lowwercase'
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path_to_file}
        response = requests.put(file_url, headers=headers, params=params)
        status_code = response.status_code
        return status_code

    def category_delete(self, path_to_file: str):
        '''
        Данный метод удаляет каталог на Яндекс.диске. На вход получает название каталога
        '''
        file_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path_to_file}
        response = requests.delete(file_url, headers=headers, params=params)
        status_code = response.status_code
        return status_code



with open('tokenYa.txt', 'r') as file_object:
            tokenYa = file_object.read().strip()
ya = YaDisk(tokenYa)




