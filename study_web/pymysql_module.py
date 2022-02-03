import pymysql

# 1、连接数据库（创建连接对象）
# 参数
# host : 连接 mysql 的主机   port : 连接端口   user : 用户名   password : 密码   database : 数据库名称   charset : 编码
conn = pymysql.connect(host='localhost', port=3306, user='root', password='199108', database='jing_dong', charset='utf8')

# 2、创建游标对象
cur = conn.cursor()

# 3、执行 sql 语句
cur.execute("select * from goods;")

# 4、获取数据
data = cur.fetchall()
print(data)

# 5、关闭对象
cur.close()
conn.close()