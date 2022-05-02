nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

def flat_generator(list):
    cursor_1 = 0
    cursor_2 = 0
    while cursor_1 < len(list):
        while cursor_2 < len(list[cursor_1]):
            yield list[cursor_1][cursor_2]
            cursor_2 += 1
        cursor_2 = 0
        cursor_1 += 1


if __name__ == '__main__':
  flat_list = [item for item in flat_generator(nested_list)]
  print(flat_list)
