import numpy as np
## !!np.linspace
## !!np.arange
def looper2(start, stop, number):
    return [float(x) for x in np.linspace(start, stop, number)]

## best solution
def looper(start, stop, number):
    return list(np.linspace(start,stop,number))

#print(looper(1,5,1), [1.0])
#print(looper(1,5,2), [1.0, 5.0])
#print(looper(1,5,3), [1.0, 3.0, 5.0])
#print(looper(1,5,4), [1.0, 2.333333333333333, 3.6666666666666665, 5.0])
#print(looper(1,5,5), [1.0, 2.0, 3.0, 4.0, 5.0])

# ellapsed time : 23min

#started at 3:00
## !! list to string : ''.join(list)
def re_ordering2(text):
    arr = text.split(' ')
    for i,x in enumerate(arr) :
        if(x[0].isupper()) :
            del arr[i]
            arr.insert(0, x)
    return ','.join(arr)
# finished 3:10
## !!sorted(name, key) i don't get it
def re_ordering(name):
    return ' '.join(sorted(name.split(), key=str.islower))


BASIC_TESTS = [
    ('ming Yao', 'Yao ming'),
    ('Mano donowana', 'Mano donowana'),
    ('wario LoBan hello', 'LoBan wario hello'),
    ('bull color pig Patrick', 'Patrick bull color pig'),
    ('jojo ddjajdiojdwo ana G nnibiial', 'G jojo ddjajdiojdwo ana nnibiial'),
    ('is one of those rare names that s both exotic and simple Adira',
     'Adira is one of those rare names that s both exotic and simple'),
    ('is an older name than annabel Amabel and a lot more distinctive',
     'Amabel is an older name than annabel and a lot more distinctive')
]

for input_str, result in BASIC_TESTS:
    print(re_ordering(input_str), result)

def warn_the_sheep(queue):
    pass
(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
(warn_the_sheep(['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
(warn_the_sheep(['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
(warn_the_sheep(['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')