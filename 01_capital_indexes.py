"""
Capital indexes
Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in 
the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

"""
capital_indexes  adında bir fonksiyon yazın.
Bu fonksiyon bir adet parametre alsın, parametrenin türü string olsun.
Fonksiyon bir liste dönsün, bu listede parametre olarak verdiğimiz string 
içindeki büyük harflerin indeksleri olsun.

Mesela,
capital_indexes("HeLlO")
fonksiyonunu çağırdığımızda, [0, 2, 4] listesi dönmeli.

"""
# https://pythonprinciples.com/challenges/Capital-indexes/


def capital_indexes(text):
    my_list = []
    for i, j in enumerate(text):
        if j.isupper():
            my_list.append(i)
    return my_list

"""----------------------------------------------------------------------------"""

# naive solution
def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

# shorter version
from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]

# you can also use the .isupper() string method.