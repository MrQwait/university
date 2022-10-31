import math
def deg_to_gms(a):
    '''
    :param a: получаем на вход десятичные градусы
    :return: возвращает целое значение градусов, минуты, секунды
    '''
    cg=int(a)
    m=int((a-cg)*60)
    s=((((a-cg)*60)-m)*60)
    s=round(s,5)
    return f'{cg}° {m}` {s}``'
def gms_to_deg(cg, m ,s):
    '''
    :param cg:
    :param m:
    :param s:
    получаем на вход целое значение градусов, минут, секунд
    :return:
    возвращает градусы
    '''
    g=cg + m/60 + s/3600
    return g
def deg_to_rad(g):
    '''
    :param g: получаем на вход градусы
    :return: возвращает радианы
    '''
    r=g*math.pi/180
    return r
def rad_to_deg(r):
    '''
    :param r: получаем на вход радианы
    :return: возвращает градусы
    '''
    g=r*180/math.pi
    return g
if __name__=='__main__':
    print(deg_to_gms(23.564523))
    print(gms_to_deg(23, 33 ,52.2828))
    print(deg_to_rad(23.564523))
    print(rad_to_deg(0.41127851301193175))
