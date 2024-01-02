def update_dict_recursive(my_dict, keys='None'):
    if keys is 'None':
        keys = list(my_dict.keys())
    if not keys:
        return
    key = keys[0]
    my_dict[key] = 1
    update_dict_recursive(my_dict, keys[1:])

my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dict_recursive(my_dict, ['a', 'b'])
print(my_dict)
