# 读取信息表格案例
from os import system


# 学生类
class Student:
    def __init__(self, name, number, score1, score2, score3):
        self.name = name
        self.number = number
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def get_stu(self):
        return f'{self.name}    {self.number}    {self.score1}    {self.score2}    {self.score3}'
        # return '%-3s    %11s    %2s    %2s    %2s' % (self.name, self.number, self.score1, self.score2, self.score3)

    def get_sum(self):
        return float(self.score1) + float(self.score2) + float(self.score3)


# 读取学生信息
fa = open('student.txt', 'a', encoding='utf-8')
fa.close()
fr = open('student.txt', encoding='utf-8')
list_stu = []
for line in fr:  # 对文件 fr 按行遍历
    l = ''.join(line.split('\n')).split('    ')  # 先去除末尾的回车，再切割
    stu = Student(l[0], l[1], l[2], l[3], l[4])  # 创建学生对象
    list_stu.append(stu)  # 学生对象添加到列表
fr.close()


# 更新文件信息
def update():
    fw = open('student.txt', 'w', encoding='utf-8')
    for s in list_stu:
        fw.write(s.get_stu() + '\n')
    fw.close()


# 继续与退出
def quit():
    opp = input("\n输入'0'退出\n输入任意键继续...\n")
    if opp == '0':
        exit()
    system('clear')


# 添加学生信息
def add_stu():
    name = input('请输入学生姓名：')
    number = input('请输入学生学号：')
    score1 = input('请输入学生语文成绩：')
    score2 = input('请输入学生数学成绩：')
    score3 = input('请输入学生英语成绩：')
    stu = Student(name, number, score1, score2, score3)
    list_stu.append(stu)
    print('添加成功！')
    fa = open('student.txt', 'a', encoding='utf-8')
    fa.write(stu.get_stu() + '\n')
    fa.close()
    quit()


# 查找学生信息
def find_stu():
    key = input('请输入关键词：')
    i = 0
    l_key = key.split(' ')
    l = len(l_key)
    flag = False
    for stu in list_stu:
        if l == 1:
            flag = key in stu.name or key in stu.number
        if l == 2:
            flag = (l_key[0] in stu.name and l_key[1] in stu.number) or (
                        l_key[1] in stu.name and l_key[0] in stu.number)
        if flag:
            i += 1
            if i == 1:
                print('\n查询到如下学生信息：')
            print(f'{i}、{stu.get_stu()}')
    if i == 0:
        print(f'\n查询不到与"{key}"相关的学生信息！')
    quit()


# 修改学生信息
def revise_stu():
    key = input('请输入关键词：')
    if key == '':
        print(f'\n查询不到与"{key}"相关的学生信息！')
        quit()
        return
    i = 0
    l_key = key.split(' ')
    l = len(l_key)
    flag = False
    for stu in list_stu:
        if l == 1:
            flag = key in stu.name or key in stu.number
        if l == 2:
            flag = (l_key[0] in stu.name and l_key[1] in stu.number) or (
                        l_key[1] in stu.name and l_key[0] in stu.number)
        if flag:
            i += 1
            if i == 1:
                print('\n查询到如下学生信息：')
            print(f'{i}、{stu.get_stu()}')
            op0 = input('是否为正确的修改对象(Y/N):\n')
            if op0 == 'Y' or op0 == 'y':
                print('\n操作列表：\n1、姓名\n2、学号\n3、语文成绩\n4、数学成绩\n5、英语成绩\n6、修改全部\n0、取消修改')
                op1 = input('请输入操作选项：')
                if op1 == '0':
                    break
                elif op1 == '1':
                    stu.name = input('\n请输入新的学生姓名：')
                elif op1 == '2':
                    stu.name = input('\n请输入新的学生学号：')
                elif op1 == '3':
                    stu.score1 = input('\n请输入新的语文成绩：')
                elif op1 == '4':
                    stu.score2 = input('\n请输入新的数学成绩：')
                elif op1 == '5':
                    stu.score3 = input('\n请输入新的英语成绩：')
                elif op1 == '6':
                    stu.name = input('\n请输入新的学生姓名：')
                    stu.name = input('\n请输入新的学生学号：')
                    stu.score1 = input('\n请输入新的语文成绩：')
                    stu.score2 = input('\n请输入新的数学成绩：')
                    stu.score3 = input('\n请输入新的英语成绩：')
                print('修改成功！')
                update()
                break
    if i == 0:
        print(f'\n查询不到与"{key}"相关的学生信息！')
        quit()
        return
    quit()


# 删除学生信息
def delete_stu():
    key = input('请输入关键词：')
    if key == '':
        print(f'\n查询不到与"{key}"相关的学生信息！')
        quit()
        return
    i = 0
    l_key = key.split(' ')
    l = len(l_key)
    flag = False
    for stu in list_stu:
        if l == 1:
            flag = key in stu.name or key in stu.number
        if l == 2:
            flag = (l_key[0] in stu.name and l_key[1] in stu.number) or (
                        l_key[1] in stu.name and l_key[0] in stu.number)
        if flag:
            i += 1
            if i == 1:
                print('\n查询到如下学生信息：')
            print(f'{i}、{stu.get_stu()}')
            op0 = input('是否为正确的删除对象(Y/N):\n')
            if op0 == 'Y' or op0 == 'y':
                list_stu.remove(stu)
                update()
                print('删除成功！')
                break
    if i == 0:
        print(f'\n查询不到与"{key}"相关的学生信息！')
        quit()
        return
    quit()


# 按总成绩排序
def sort_stu():
    l = len(list_stu)
    if l == 0:
        print('\n还没有学生信息，请先添加学生信息噢！')
        quit()
        return
    for i in range(1, l):
        for j in range(0, l - i):
            if list_stu[j].get_sum() < list_stu[j + 1].get_sum():
                temp = list_stu[j]
                list_stu[j] = list_stu[j + 1]
                list_stu[j + 1] = temp
    print('\n排序完毕！')
    update()
    quit()


# 查看所有学生信息
def all_stu():
    i = 0
    for stu in list_stu:
        i += 1
        print('%2d、%s' % (i, stu.get_stu()))
    if i == 0:
        print('\n还没有学生信息，请先添加学生信息噢！')
    quit()


# 操作面板
system('clear')
while True:
    print('========欢迎来到学生管理系统========')
    print('====      1、添加学生信息       ====')
    print('====      2、查找学生信息       ====')
    print('====      3、修改学生信息       ====')
    print('====      4、删除学生信息       ====')
    print('====      5、按总成绩排序       ====')
    print('====      6、查看所有学生       ====')
    print('====      0、退出系统           ====')
    print('====================================')
    op = input('请输入您的操作选项：')
    if op == '0':
        print('感谢使用！')
        break
    elif op == '1':
        add_stu()
    elif op == '2':
        find_stu()
    elif op == '3':
        revise_stu()
    elif op == '4':
        delete_stu()
    elif op == '5':
        sort_stu()
    elif op == '6':
        all_stu()
    else:
        print('\n输入错误！')
        quit()
