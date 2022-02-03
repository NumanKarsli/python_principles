"""
Anagrams
Two strings are anagrams if you can make one from the other by rearranging the letters.
Write a function named is_anagram that takes two strings as its parameters. 
Your function should return True if the strings are anagrams, and False otherwise.
For example, the call is_anagram("typhoon", "opython") should return True while
 the call is_anagram("Alice", "Bob") should return False.
"""

"""
Aynı harflerle yazılan ama harfleri yer değiştirince ayrı anlama gelen sözcük, mesela
bahri ile ihbar kelimeleri...
is_anagram adında, iki adet string parametre alan bir fonksiyon yazın.
Fonksiyonunuz eğer stringler anagram ise True, değilse False dönmelidir.
Mesela is_anagram("typhoon", "opython") çağrıldığında True,
call is_anagram("Alice", "Bob") çağrıldığında False dönmelidir.
"""
# https://pythonprinciples.com/challenges/Anagrams/


def is_anagram(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    return list1 == list2

"""----------------------------------------------------------------------------"""

# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)