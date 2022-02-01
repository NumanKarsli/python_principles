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


# Numan burayı değiştirdi
#Bursaıda github'dan değiştirildi
