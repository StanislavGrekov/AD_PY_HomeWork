 # 1 Задание
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter_element = 0
        self.counter_list = 0
        return self

    def __next__(self):
            try:
                if len(self.list_of_list[self.counter_list]) == self.counter_element:
                    self.counter_list += 1
                    self.counter_element = 0
                item = self.list_of_list[self.counter_list][self.counter_element]
                self.counter_element += 1
                return item
            except IndexError:
                raise StopIteration

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    count = 0
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        count+=1
        assert flat_iterator_item == check_item
        print(f'test №{count} pass')

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print('List Test pass')


if __name__ == '__main__':
    test_1()


#2 Задание
import types

list_of_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

def flat_generator(list_of_lists):
    try:
        counter = 0
        my_list = []
        while True:
            my_list.extend(list_of_lists[counter])
            counter+=1
            if counter == len(list_of_lists):
                while True:
                    yield my_list.pop(0)
    except IndexError:
       pass


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print(isinstance(flat_generator(list_of_lists_1), types.GeneratorType))

if __name__ == '__main__':
    test_2()


#3 Задание (конечно, выполненно совсем неоптимально. Временни нет причесывать)
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_of_list_copy = []
        self.my_list = []

    def __iter__(self):
        self.count = 0
        self.count_element = 0
        self.count_return = 0
        return self

    def __next__(self):
        self.list_of_list_copy = self.list_of_list.copy()
        while True:
            if len(self.list_of_list_copy) != self.count_element:
                try:
                    next_item = self.list_of_list_copy[self.count]
                    self.count +=1
                except IndexError:
                    self.count = 0
                    self.count_element = 0
                    self.list_of_list_copy = self.my_list.copy()
                    self.my_list = []
                    continue
                if isinstance(next_item, list):
                    self.my_list.extend(next_item)
                else:
                    self.my_list.append(next_item)
                    self.count_element += 1
            else:
                try:
                    item = self.list_of_list_copy[self.count_return]
                    self.count_return +=1
                    return item
                except IndexError:
                    raise StopIteration

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    count = 0
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item
        print(f'test №{count} pass')
        count +=1

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print(list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!'])


if __name__ == '__main__':
    test_3()


#4 Задание
import types

def flat_generator(list_of_list):
    try:
        list_of_list_copy = list_of_list.copy()
        my_list = []
        while True:
            count = 0
            for element in list_of_list_copy:
                if isinstance(element, list):
                    my_list.extend(element)
                else:
                    my_list.append(element)
                    count +=1
            list_of_list_copy = my_list.copy()
            my_list = []
            if len(list_of_list_copy) == count:
                raise SystemError
    except SystemError:
        for element in list_of_list_copy:
            yield element


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    count = 0
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item
        print(f'test №{count} pass')
        count +=1

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()