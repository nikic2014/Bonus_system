import eel
from random import randint

data = {}

def rewrite_txt():
    f = open('data.txt', 'w+', encoding="utf-8")
    for i in data.keys():
        str = i + ';' + ';'.join(data[i]) + ';'
        print(str)
        f.write(str + "\n")
    f.close()

def read_data():
    f = open('data.txt', 'r', encoding="utf-8")
    lst = f.readlines()
    print('lst =',lst, '\n')

    ############################################ Добавление пользователя в словарь
    flag_correct_data_file = 1
    for str in lst:
        info = str.split(';')
        if info[0] not in data.keys():
            data[info[0]] = info[1:-1]
        else:
            print(f"Файл данных некоректный, полльзователь {info[0]} встречается 2 раза")
            flag_correct_data_file = 0
    f.close()
    ############################################ Перезапись файла если есть повторения
    rewrite_txt()


read_data()

@eel.expose
def write_data(str):
    ############################################ добавляем пользователя str
    print('str =',str, '\n')
    f = open('data.txt', 'a', encoding="utf-8")
    info = str.split(';')
    print('intfo =', info, '\n')

    ############################################ проверка существует ли такой пользователь
    flag = 0
    if info[0] not in data.keys():
        data[info[0]] = info[1:-1]
        f.write(str + "\n")
    else:
        flag = 1
    f.close()

    print('flag добавляемый пользователь уже есть =', flag, '\n')
    return flag

@eel.expose
def find_user(key):
    print(data.keys())
    if key in data.keys():
       return ';'.join([key] + data[key])
    return 'no user'

@eel.expose
def inc_dec(key, count, pl_mn):
    d = count.split(' ')
    ans = 0
    if (pl_mn > 0):
        ans = str(float(data.get(key)[-2]) + 0.05 * int(count))
    else:
        ans = str(float(data.get(key)[-2]) - float(d[1]))
    data[key][-2] = ans
    print(ans)
    return ans

def test():
    for i in range(100000):
        write_data(str(randint(10000000000, 90000000000)) + ';asdf;adfs;afds;21.09.2002;0;0;')


if __name__ == '__main__':
    try:
        ############################################ тест времени на 100к пользователей
        #test()
        eel.init("web")
        eel.start("index.html", size=(900, 850))
    finally:
        rewrite_txt()



#https://sms.ru/sms/send?api_id=2C70B7B8-C558-7013-6FA9-687CE0094B94&to=79085561046&msg=привет,+как+дела?&json=0&from=VEDANO
#