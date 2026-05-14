my_dict = {
    'tuple': (1, 8, False, 'apple', 2.99),
    'list': [5, 9, 'orange', 4.28, True],
    'dict': {
        'one': 'banana',
        2: 2,
        'three': 3.98,
        'four': [1, 'mango', 8],
        'five': 'lime'
    },
    'set': {8, 3, 'lemon', True, None}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(3)
my_dict['list'].pop(1)

my_dict['dict'][('i am a tuple',)] = 'pomelo'
my_dict['dict'].pop('four')

my_dict['set'].add('apricot')
my_dict['set'].remove(8)

print(my_dict)
