import os
import datetime

#####1 Задание #########
def logger(old_function):

    def new_function(*args,**kwargs):
        try:
            arg_1 = args[0]
            arg_2 = args[1]
            day_time= datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
            result = old_function(*args)
            main = open('main.log', 'a', encoding='utf-8')
            main.write(f"Дата и время выполнения: {day_time}, имя функции: {old_function} аргумент №1: {arg_1}, аргумент №2: {arg_2}, возвращаемое значение: {result}\n")
            main.close()
            return result
        except IndexError:
            try:
                arg_1 = args[0]
                for key,values in kwargs.items():
                    arg_2 = values
                day_time = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
                result = old_function(*args,**kwargs)
                main = open('main.log', 'a', encoding='utf-8')
                main.write(
                    f"Дата и время выполнения: {day_time}, имя функции: {old_function} аргумент №1: {arg_1}, аргумент №2: {arg_2}, возвращаемое значение: {result}\n")
                main.close()
                return result
            except:
                arg_1 = kwargs['a']
                arg_2 = kwargs['b']
                day_time = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
                result = old_function(*args, **kwargs)
                main = open('main.log', 'a', encoding='utf-8')
                main.write(
                    f"Дата и время выполнения: {day_time}, имя функции: {old_function} аргумент №1: {arg_1}, аргумент №2: {arg_2}, возвращаемое значение: {result}\n")
                main.close()
                return result

    return new_function

def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()


######2 Задание #########
def logger(path):
    def __logger(old_function):
        def new_function(*args,**kwargs):
            try:
                arg_1 = args[0]
                arg_2 = args[1]
                day_time= datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
                result = old_function(*args)
                main = open(path, 'a', encoding='utf-8')
                main.write(f"Дата и время выполнения: {day_time}, имя функции: {old_function} аргумент №1: {arg_1}, аргумент №2: {arg_2}, возвращаемое значение: {result}\n")
                main.close()
                return result
            except IndexError:
                pass
                try:
                    arg_1 = args[0]
                    for key,values in kwargs.items():
                        arg_2 = values
                    day_time = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")
                    result = old_function(*args,**kwargs)
                    main = open(path, 'a', encoding='utf-8')
                    main.write(
                        f"Дата и время выполнения: {day_time}, имя функции: {old_function} аргумент №1: {arg_1}, аргумент №2: {arg_2}, возвращаемое значение: {result}\n")
                    main.close()
                    return result
                except:
                    pass
        return new_function
    return __logger

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)
    for path in paths:
        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()