def only_ints(a, b):
    if type(a) == type(b) == int:
        return True

    else:
        return False

print(only_ints(1, 2))