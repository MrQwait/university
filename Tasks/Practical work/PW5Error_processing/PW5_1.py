def error_options(a):
    '''
    :param a: файл
    :return: список чисел
    '''
    try:
        f=open(a)
        f.readline()
        str: list[str] = f.readlines()
        if len(str)==0:
            print('Не тот файл')
        else:
            for i in range(len(str)):
                str[i]=str[i].replace('\n','')
                str[i]=int(str[i])
            print(str)
            #break
    except FileNotFoundError:
        print('Такого файла нет')
    except ValueError:
        print('Не только целые числа')
    finally:
        try:
            f.close()
        except:
            print('Файл не открывался')

error_options(input())

