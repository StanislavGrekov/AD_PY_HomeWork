import pytest
import unittest
from parameterized import parameterized
from main import geo_, geo_logs #1 Задание, 1 упражнение
from main import  ids_,ids #1 Задание, 2 упражнение
from main import queries_, queries #1 Задание, 3 упражнение
from main import YaDisk, ya, tokenYa #2 Задание
from main1 import selenium_func #3 Задание

############################################## 1 задание, упражнение 1 #############################################
#Тестирование с помощью unittest:
class TestFunc(unittest.TestCase):

    def test_geo(self):
        result = geo_(geo_logs)
        etalon = 'Россия'
        for element in result:
            for values in element.values():
                self.assertEqual(values[1],etalon)

#Тестирование с помощью pytest:
def test_geo():
        result = geo_(geo_logs)
        etalon = 'Россия'
        for element in result:
            for values in element.values():
                assert values[1]==etalon

############################################# 1 задание, упражнение 2 #############################################


FIXTURE = [(98,ids_(ids)[0]), (35,ids_(ids)[1]), (15,ids_(ids)[2]),(213,ids_(ids)[3]),(54,ids_(ids)[4]),(119,ids_(ids)[5])]

#Тестирование с помощью unittest:
class TestFunc(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_ids_(self,a,b):
        self.assertEqual(a,b)

#Тестирование с помощью pytest:
def test_ids_():
        result = ids_(ids)
        etalon = [98, 35, 15, 213, 54, 119]
        count = 0
        for element in result:
            assert element==etalon[count], 'Здесь может быть текст'
            count +=1

############################################## 1 задание, упражнение 3 #############################################

etalon_list = [42.86, 28.57, 28.57, 28.57, 42.86, 42.86, 42.86]

# Тестирование списков с помощью unittest без параметризации
class TestFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def test_queries_(self):
        self.assertEqual(queries_(queries), etalon_list)

#Тестирование списков с помощью pytest с использоваием класса и параметризации:
@pytest.mark.parametrize("return_,etalon", [(queries_(queries), etalon_list)])
class TestClass:
    def test_queries_(self, return_, etalon):
        assert return_ == etalon, 'значения не равны'

############################################## 2 задание #############################################
# Провереряем, что имя папки, создаваемой на яндекс диске, удовлетворяет требованиям: длинна меньше 5 символов, не состоит из цифр,
#используются только заглавные буквы. Далее мы проверяем статус-код создания и удаления папки.

def test_YaDisk_():
    # Имя папки больше 4 символов
    result = ya.category_created('ABCDE')
    etalon = 'len name of folder > 4'
    assert result == etalon
    # Имя папки только цифры
    result = ya.category_created('1234')
    etalon = 'digit'
    assert  result == etalon
    # Имя папки только маленькие буквы
    result = ya.category_created('abcd')
    etalon = 'lowwercase'
    assert  result == etalon
    #Проверка создания папки
    result = ya.category_created('TEST')
    etalon = 201
    assert result == etalon
    # Проверка повторного создания папки
    result = ya.category_created('TEST')
    etalon = 409
    assert result == etalon
    # Удаление папки
    result = ya.category_delete('TEST')
    etalon = 204
    assert result == etalon
    # Повторное удаление папки
    result = ya.category_delete('TEST')
    etalon = 404
    assert result == etalon

# Повторяем тоже самое только с использованием параметризации.

FIXTURE = [('ABCDE','len name of folder > 4'),('1234','digit'),('abcd','lowwercase'),('TEST',201),('TEST',409)]

@pytest.mark.parametrize('result, etalon', FIXTURE)
def test__YaDisk_create(result, etalon):
        result = ya.category_created(result)
        assert result == etalon

FIXTURE = [('TEST',204),('TEST',404)]

@pytest.mark.parametrize('result, etalon', FIXTURE)
def test__YaDisk_delete(result, etalon):
        result = ya.category_delete(result)
        assert result == etalon

########################################### 3 задание ##########################################
#Проверяем работу функции selenium_func() из модуля main1

FIXTURE = [('NavigationLink_root__E9oll', '// *[ @ id = "__next"] / div / main / div / div[2] / div[2] / div / a[4]', 'Главная', 'Мои контакты')]

@pytest.mark.parametrize('class_, xpat_, etalon1, etalon2', FIXTURE)
def test_Selenium(class_, xpat_, etalon1, etalon2):
        result = selenium_func(class_, xpat_)
        assert result[0] == etalon1
        assert result[1] == etalon2

