''':cvar

'''
import mysql.connector
import time
import os

def read_file(file_name):
    tempr = '00000000'
    try:
        with open(file_name) as f: 
            for f_line in f:
                list_data = split_data(f_line)
                for list_char in list_data:
                    if len(list_char) > 36:
                        if list_char[0] == '0' and list_char[1] == '9' and list_char[21] == '3':
                            i = 28
                            tempr = ''
                            while i < 36:
                                tempr = tempr + list_char[i]
                                i += 1
    except IOError:
        print('File not exist, try again later.')
    return tempr

def split_data(contents):
    splited_data = contents.split(' ')
    return(splited_data)

def mysql_insert(temperature, humidity):
    conn = mysql.connector.connect(user='username', password='password', database='your_database')
    cursor = conn.cursor()
    cursor.execute('insert into your_table (temperature, humidity) values (%s, %s)', [str(temperature), str(humidity)])
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    i = 0
    t_and_h_ext = '00000000'
    while True:
        if i > 20:
            i = 0
        t_and_h = read_file('mylog.txt')
        if t_and_h == '00000000':
            t_and_h = t_and_h_ext
        else:
            t_and_h_ext = t_and_h
        list_t_and_h = list(t_and_h)
        t1 = list_t_and_h[0] + list_t_and_h[1]
        t2 = list_t_and_h[2] + list_t_and_h[3]
        h1 = list_t_and_h[4] + list_t_and_h[5]
        h2 = list_t_and_h[6] + list_t_and_h[7]
        float_t = int(t1, 16) + float(int(t2, 16))/100
        float_h = int(h1, 16) + float(int(h2, 16))/100
        mysql_insert(float_t, float_h)
        os.popen('rm -f logbak/mylog{}.txt'.format(str(i)))
        os.popen('cp mylog.txt logbak/mylog{}.txt'.format(str(i)))
        i += 1
        time.sleep(60)
