class Stack():
    def __init__(self,list_):
        self.list_ = list_

    def isEmpty(self):
        if len(self.list_) != 0:
            return True
        else:
            return False

    def push(self,element):
        self.list_.append(element)

    def pop(self):
        last_element = self.list_.pop()
        return last_element

    def peek(self):
        last_element = self.list_.pop()
        self.list_.append(last_element)
        return last_element

    def size(self):
        return len(self.list_)

#Функция проверки балансировки
def stack_(sequence: str):
    list_ = []
    stack = Stack(list_)
    list_sequence = [i for i in sequence]
    stack_sequence = Stack(list_sequence)
    while stack_sequence.isEmpty():
        try:
            element_peek = stack.peek()
            element_pop = stack_sequence.pop()
            stack.push(element_pop)
            if (element_peek == '}' and element_pop  == '{') or (element_peek == ')' and element_pop  == '(') or (element_peek == ']' and element_pop  == '['):
                stack.pop()
                stack.pop()
        except:
            element_pop = stack_sequence.pop()
            stack.push(element_pop)

    if stack.size() == 0:
        return 'Сбалансированно'
    else:
        return "Несбалансированно"


balance = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}']
no_balance = ['}{}', '{{[(])]}}','[[{())}]']

def test():
    for element in balance:
        assert stack_(element) == 'Сбалансированно'
    for element in no_balance:
        assert stack_(element) == "Несбалансированно"

if __name__=="__main__":
    test()


