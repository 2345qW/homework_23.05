list1 =[1,2,3,4,5]
list2 = ['a','q','g','f','w']
def list_dict (list1,list2):
    if len(list1)==len(list2):
        dic =dict(zip(list1,list2))
    return dic
print(list_dict(list1,list2))