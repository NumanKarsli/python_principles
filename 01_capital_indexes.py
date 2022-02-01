def capital_indexes(text):
    my_list = []
    for i, j in enumerate(text):
        if j.isupper():
            my_list.append(i)
    return my_list