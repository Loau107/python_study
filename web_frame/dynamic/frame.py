# 函数列表
import datetime
import json

import pymysql

func_list = {}


# 路由装饰器
def route(path):

    def func_outer(func):
        func_list[path] = func

        def func_inner():
            func()
        return func_inner
    return func_outer


# 一个函数控制一个页面（切面化编程）
@route('/index.html')
def index():
    with open('template/index.html') as f:
        file_data = f.read()
    return file_data


@route('/center.html')
def center():
    # 获取　html 数据
    with open('template/center.html') as f:
        file_data = f.read()
    # 获取数据库数据
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='199108', database='jing_dong', charset='utf8')
    cur = conn.cursor()
    cur.execute("select id, name, cate_name, brand_name, price from goods;")
    goods_data = cur.fetchall()
    cur.close()
    conn.close()
    # html 格式
    temp = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
    '''
    html = ''
    for good in goods_data:
        html += temp % (good[0], good[1], good[2], good[3], good[4])
    file_data = file_data.replace('{%content%}', html)
    return file_data


@route('/time.html')
def index():
    with open('template/time.html') as f:
        file_data = f.read()
    return file_data


@route('/time_data.html')
def time_data():
    # 按照 json 格式要求组装数据 [{}, {} ... {}]
    d = datetime.datetime.now()
    time = [{'time':f'{d.year}-{d.month}-{d.day} {d.hour}:{d.minute}:{d.second}'}]
    time = json.dumps(time)
    return time


# 接口
def application(path):
    try:
        func = func_list[path]
        return func()
    except Exception as e:
        print(e)
        return 'not found'
