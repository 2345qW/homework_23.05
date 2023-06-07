dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5,}
def common_elements (dic1,dic2):
    key_list=[]
    for key in dic1:
        for key2 in dic2:
            if key ==key2:
                if dic1[key]==dic2[key2]:
                    key_list.append(key)
    print(f'Спільні ключі з однаковими значеннями:{key_list}')
common_elements(dict1,dict2)