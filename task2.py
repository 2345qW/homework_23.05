str1="apple banana apple cherry banana apple"

def word_count (str_):
    list1 = str_.split(' ')
    dic ={}
    for element in list1:
        if element in dic:
            dic[element]=dic[element]+1
        else:
            dic.update({element:1})
    return(dic)
print(word_count(str1))