import pymysql
'''
# 1、连接数据库（创建连接对象）
# 参数
# host : 连接 mysql 的主机   port : 连接端口   user : 用户名   password : 密码   database : 数据库名称   charset : 编码
conn = pymysql.connect(host='localhost', port=3306, user='root', password='199108', database='jing_dong', charset='utf8')

# 2、创建游标对象
cur = conn.cursor()

# 3、执行 sql 语句
cur.execute('update goods set price = 3399 where id = 1;')

# 4、提交修改
# 如果不提交修改 程序的修改的数据不会真正更新到数据库中
conn.commit()

# 4、获取数据
cur.execute('select * from goods')
data = cur.fetchall()
for line in data:
    print(line)

# 5、关闭对象
cur.close()
conn.close()
'''



# sql 注入
conn = pymysql.connect(host='localhost', port=3306, user='root', password='199108', database='jing_dong', charset='utf8')
cur = conn.cursor()
# 获取指定商品信息
name = input('请输入商品名称：')
# cur.execute(f'select * from goods where name = "{name}";')
# 当用户输入 "or 1 or" 的时候，可以查询出所有的商品信息
# 防 sql 注入写法
cur.execute('select name, cate_name, brand_name, price from goods where name = %s;', [name])
data = cur.fetchall()
for line in data:
    print(line)
cur.close()
conn.close()



