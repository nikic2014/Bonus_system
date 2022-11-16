
import eel
from random import randint
from datetime import datetime
import requests

data = {}



def rewrite_txt(file):
    f = open(file, 'w+', encoding="utf-8")
    for i in data.keys():
        str = i + ';' + ';'.join(data[i]) + ';'
        #print(str)
        f.write(str + "\n")
    f.close()

def read_data(file):
    f = open(file, 'r', encoding="utf-8")
    lst = f.readlines()
    #print('lst =',lst, '\n')

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
    rewrite_txt('data.txt')
    print(data)
    return data

refill_balance = 1

def congratulate():
    global refill_balance
    today = datetime.today()
    str_day = today.date()
    for i in data.keys():
        if refill_balance:
            day_of_born = data[i][3].split('.')
            if data[i][5] == '0' and int(day_of_born[0]) == int(str_day.day) and int(day_of_born[1]) == int(str_day.month):
                number = str(i)
                #print(number)
                f = open('sms.txt', 'r', encoding="utf-8")
                lst = f.readlines()
                sms = (' '.join(lst)).replace('\n', ' ')
                sms = sms.replace(' ', '+')
                #print(sms)
                f.close()
                zapros = f'https://sms.ru/sms/send?api_id=2C70B7B8-C558-7013-6FA9-687CE0094B94&to={number}&msg={sms}&json=0&from=VEDANO'
                #print(zapros)
                response = requests.get(zapros)
                if (str(response.text) == str('201\n')):
                    balance = 0
                else:
                    balance = response.text.split('=')[1]
                    data[i][5] = '1'
                if float(balance) < 10:
                    refill_balance = 0
            else:
                if not (int(day_of_born[0]) == int(str_day.day) and int(day_of_born[1]) == int(str_day.month)):
                    data[i][5] = '0'



@eel.expose
def write_data(str):
    ############################################ добавляем пользователя str
    #print('str =',str, '\n')
    f = open('data.txt', 'a', encoding="utf-8")
    info = str.split(';')
    #print('intfo =', info, '\n')

    ############################################ проверка существует ли такой пользователь
    flag = 0
    if info[0] not in data.keys():
        data[info[0]] = info[1:-1]
        f.write(str + "\n")
    else:
        flag = 1
    f.close()

    #print('flag добавляемый пользователь уже есть =', flag, '\n')
    return flag

@eel.expose
def find_user(key):
    #print(data.keys())
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
    #print(ans)
    return ans

@eel.expose
def del_user(key):
    print(data[key])
    try:
        del data[key]
        return "good"
    except:
        return "not good"

@eel.expose
def check_info():
    zapros = "https://sms.ru/my/balance?api_id=2C70B7B8-C558-7013-6FA9-687CE0094B94&json=0"
    response = requests.get(zapros)
    ans = response.text.split('\n')
    return (ans[1])

def test():
    for i in range(100000):
        write_data(str(randint(10000000000, 90000000000)) + ';asdf;adfs;afds;21.09.2002;0;0;')


if __name__ == '__main__':
    try:
        ############################################ тест времени на 100к пользователей
        #test()

        read_data('data.txt')
        congratulate()
        eel.init("web")
        eel.start("index.html", size=(900, 850))
    finally:
        rewrite_txt('data.txt')



#https://sms.ru/sms/send?api_id=2C70B7B8-C558-7013-6FA9-687CE0094B94&to=79085561046&msg=привет,+как+дела?&json=0&from=VEDANO