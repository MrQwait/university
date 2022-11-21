def error_options(a):
    try:
        f=open(a)
        f.readline()
        s=f.readlines()
        if len(s)==0:
            print('Не тот файл')
        else:
            for i in range(len(s)):
                s[i]=s[i].replace('\n','')
                s[i]=int(s[i])
            print(s)
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

