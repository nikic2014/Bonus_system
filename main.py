import eel

data = {}

def read_data():
    f = open('data.txt', 'r', encoding="utf-8")
    lst = f.readlines()
    print(lst)
    for str in lst:
        info = str.split(';')
        if info[0] not in data.keys():
            data[info[0]] = info[1:-1]
        else:
            print('u r пидр')
    f.close()

read_data()

@eel.expose
def write_data(str):
    print(str)
    f = open('data.txt', 'a', encoding="utf-8")
    info = str.split(';')
    print(info)
    flag = 0
    if info[0] not in data.keys():
        data[info[0]] = info[1:-1]
        f.write(str + "\n")
    else:
        flag = 1
    f.close()
    return flag

@eel.expose
def find_user(key):
    print(data.keys())
    if key in data.keys():
       return ';'.join([key] + data[key])
    return 'no user'

@eel.expose
def inc_dec(key, count, pl_mn):
    ans = str(int(data.get(key)[-1]) + int(pl_mn) * int(count))
    data[key][-1] = ans
    print(ans)
    return ans



eel.init("web")
eel.start("index.html", size = (900, 850))


#https://sms.ru/sms/send?api_id=2C70B7B8-C558-7013-6FA9-687CE0094B94&to=79085561046&msg=привет,+как+дела?&json=0&from=VEDANO
#