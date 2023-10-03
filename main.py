class FlatIterator:

    def __init__(self, list_of_list):
        def unpack(items: list) -> list:
            res_list = []
            for item in items:
                if type(item) == list:
                    res_list.extend(unpack(item))
                else:
                    res_list.append(item)
            return res_list
        self.list = unpack(list_of_list)

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= len(self.list):
            raise StopIteration
        else:
            return self.list[self.counter]

def unpack(items: list) -> list:
    res_list = []
    for item in items:
        if type(item) == list:
            res_list.extend(unpack(item))
        else:
            res_list.append(item)
    return res_list

def flat_generator(nested_list: list):
    for item in unpack(nested_list):
        yield item

def test_2():
    nested_list = [
        ['a', [['b'], ['c']]],
        ['d', ['e'], 'f'],
        [1, 2, None],
    ]
    for item in flat_generator(nested_list):
        print(item)

def test_1():
    list_of_lists_1 = [
        ['a', ['b'], 'c'],
        ['d', [['e'], ['f']], 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):


        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    test_2()

