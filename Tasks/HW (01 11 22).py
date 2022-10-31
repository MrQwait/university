from Work.CalculatorGrad import *

def f(*args, **kwargs):
    a=[*args]
    k=[*kwargs]
    s=[]
    for i in range(len(a)):
        s.append(f'Point_{i+1} = {deg_to_gms(a[i])}')
    for i in range(len(k)):
        s.append(f'{k[i]} = {kwargs[str(k[i])]}')
    return s


print(f(1.1,2,9,98,b=9,n=8,k=151))