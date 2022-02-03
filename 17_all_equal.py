"""
All equal
Define a function named all_equal that takes a list and checks whether all 
elements in the list are the same.
For example, calling all_equal([1, 1, 1]) should return True.
"""
"""
all_equal adında bir fonksiyon yazın. Parametre olarak bir liste alsın sonra
bu listenin tüm elemanları aynı mı diye baksın.
mesela all_equal([1, 1, 1]) çağrıldığında True dönsün.
"""

# 

def all_equal(myList):
    for i in myList:
        if i != myList[0]:
            return False
    return True

"""----------------------------------------------------------------------------"""

# naive solution
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True


# one-liner with nested list comprehension
# and the all() built-in
def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)