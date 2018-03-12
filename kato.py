import re

def f1(a1,a2):
    return a1*a1+a2

# def f1(a1,a2):
#     if a1 == 0:
#         return (0)
#     elif a1 == 1:
#         return (1)
#     elif a1 == 2:
#         return (4)
#     elif a1 == 2 and a2 == 1:
#         return a1*a1+a2
#     elif a1 == 2 and a2 == 3:
#         return a1*a1+a2

def f2(a1):
    if a1 == 'ala':
        return ('a')
    elif a1 == [1,2,3]:
        return (1)
    elif a1 == []:
        return('BUUUUM')

def f3(a1):
    s={1:'jeden', 2:'dwa', 3:'trzy'}
    return s.get(a1, 'other')

    # if a1 == 1:
    #     return ('jeden')
    # elif a1 == 2:
    #     return ('dwa')
    # elif a1 == 3:
    #     return('trzy')

def f4(a1=0,a2=0):
    if a1 == 'ala':
        return ('%s ma kota' %(a1))
    elif a2 == 'kot':
        return ('%s ma kota' %(a2))
    elif a1 == 'kot' and a2 == 'psa':
        return('%s ma kota i %s' %(a1, a2))
    elif a1 == 'kot' and a2 == 'mysz':
        return('%s ma kota i %s' %(a1, a2))

def f5(a1,a2=1):
    x = range(a1)
    return x[::a2]






def f6(a1,a2):
    return a1*a2

def f7(a1):
    if type (a1) is str and len(a1)==3:
        return ('slowo')
    elif a1<10 and a1>0 and type (a1) is int:
        return('cyfra')
    elif a1>10 and type (a1) is int:
        return('liczba')
    elif a1<0 and type (a1) is int:
        return('liczba_ze_znakiem')
    elif type (a1) is str and len(a1)>3:
        return ('zdanie')

# def f7(a1):
#     if re.match('[a-z]+',a1):
#         return('slowo')
#     elif re.match('[1-9]',a1):
#         return('cyfra')
#     elif re.match('[1-9][1-9]+',a1):
#         return('liczba')
