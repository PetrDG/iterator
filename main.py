nested_list_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

nested_list_2 = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]



# task 1 - Итератор

class FlatIterator():
    def __init__(self, user_list):
        self.list = user_list

    def __iter__(self):
        self.coursor = 0
        self.coursor_form = -1
        return self

    def __next__(self):

        if self.coursor_form < len(self.list[self.coursor]) - 1:
            self.coursor_form += 1
        else:
            self.coursor_form = 0
            self.coursor += 1

        if self.coursor == len(self.list):
            raise StopIteration

        return self.list[self.coursor][self.coursor_form]

print('Задание 1')
my_list = FlatIterator(nested_list_1)
for item in my_list:

    print(item)
print('\n')



# task 2 - Генератор

def flat_generator(user_list):
    for i in user_list:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i

print('Задание 2')
my_list = flat_generator(nested_list_2)
for i in my_list:

    print(i)
