def double_letters(a):
    letter1 = ""
    for i in a:
        if i == letter1:
            return True
        letter1 = i 
    return False