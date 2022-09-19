# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool

from types import new_class

array = []
data = open('HomeWork/homework004/task005.txt', 'r')
array = data.read()
data.close

print(array)





def in_RLE_algoritm(a:list):
    new_array = []
    i = 0
    while i < len(a)-1:
        j = i
        ind = 0
        while j < len(a)-1:
            if(a[i] == a[j]):
                j += 1
                ind += 1
            else:
                break
    
        new_array.append(ind)
        new_array.append(a[i])
        i = j
    list_array = "".join(map(str,new_array))
    return list_array
    


a = open('HomeWork/homework004/task005New.txt', 'w')
a.write(in_RLE_algoritm(array))
a.close







