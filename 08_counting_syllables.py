# https://pythonprinciples.com/challenges/Counting-syllables/
def count(string):
    sayac = 0
    for i in string:
        if i == "-":
            sayac += 1
            
    return sayac+1


# naive solution
def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))