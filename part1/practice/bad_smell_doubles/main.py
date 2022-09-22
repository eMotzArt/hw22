# Как то вечером три разработчика написали 
# три метода класса `SomeClass`, каждый под себя. 
# Методы по сути своей почти одинаковые.
#
# Напишите свой метод `sorted_func`, 
# учитывая особенности всех представленных методов


class SomeClass:
    def __init__(self):
        self._lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self, reverse=False):
        return sorted(self._lst, reverse=reverse)

example = SomeClass()
print(example.sorted_func())
print(example.sorted_func(reverse=True))
