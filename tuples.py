import random

def stringcases(string):
    str_upper = string.upper()
    str_lower = string.lower()
    str_title = string.title()
    str_rev = string[::-1]

    return str_upper, str_lower, str_title, str_rev

a, b, c, d = stringcases("test")

print(a)
print(b)
print(c)
print(d)

def combo(it_1, it_2):
    list_out = []
    for index, item in enumerate(it_1):
        tup = item, it_2[index]
        list_out.append(tup)
    print(list_out)
    return list_out

def nchoices(itt, n):
    rand_list = []
    while n > 0:
        rand_list.append(random.choice(itt))
        n -= 1
    print(rand_list)
    return rand_list


combo(['swallow', 'snake', 'parrot'], 'abc')
nchoices(['swallow', 'snake', 'parrot'],100)