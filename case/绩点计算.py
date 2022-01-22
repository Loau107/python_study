from os import system

class Student:
    def __init__(self, name, list_score, gpa):
        self.name = name
        self.list_score = list_score
        self.gpa = gpa
    def get_stu(self):
        return f'{self.name} {self.list_score} {self.gpa}'
    def get_stuGPA(self):
        return "学生: '%s':\n平均绩点: %f  无公选绩点: %f" % (self.name, self.gpa, get_GPA(self.list_score))
    def print_stu(self):
        print(f"学生: '{self.name}'")
        print('平均绩点: %.2f  无公选绩点: %.2f' % (self.gpa, get_GPA(self.list_score)))
        print(f'各科分数及学分：{self.list_score}')

def getGPA(list_score):
    if len(list_score) == 0:
        return 0
    sum = 0
    number_sum = 0
    for l_sco in list_score:
        gpa_temp = l_sco[0] / 10 - 5
        sum += gpa_temp * l_sco[1]
        number_sum += l_sco[1]
    gpa = sum / number_sum
    return gpa

def get_GPA(list_score):
    l = len(list_score)
    if l <= 1:
        return 0
    lis = []
    for i in range(l - 1):
        lis.append(list_score[i])
    sum = 0
    number_sum = 0
    for l_sco in lis:
        _gpa_temp = l_sco[0] / 10 - 5
        sum += _gpa_temp * l_sco[1]
        number_sum += l_sco[1]
    _gpa = sum / number_sum
    return _gpa

f = open('学生绩点.txt', 'a')
f.close()
with open('学生绩点.txt') as f:
    list_stu = []
    for line in f:
        lis = ''.join(line.split('\n')).split(' ')
        list_score = []
        l = len(lis)
        for i in range(1, l - 1, 2):
            l_sco = [float(lis[i]), float(lis[i + 1])]
            list_score.append(l_sco)
        list_stu.append(Student(lis[0], list_score, getGPA(list_score)))

def flush():
    with open('学生绩点.txt', 'w') as f:
        for stu in list_stu:
            line = f'{stu.name}'
            for l_sco in stu.list_score:
                line += f' {l_sco[0]} {l_sco[1]}'
            line += f' {stu.gpa}\n'
            f.write(line)

# 继续与退出
def quit():
    opp = input("\n输入'0'退出\n输入任意键继续...\n")
    if opp == '0':
        print('\n已退出！\n')
        exit()
    system('clear')

system('clear')
while True:
    op = input('1、添加学生\n2、查看绩点\n3、查看所有数据\n4、查找学生\n0、退出程序\n请输入：')
    if op == '0':
        print('\n已退出！\n')
        exit()
    elif op == '1':
        print("\n开始录入信息！\n提示：\n公选课请放到最后一科录入！！！\n输入'n'结束录入！！！\n")
        name = input("请输入学生的名字：")
        if name == 'n':
            print('已取消添加！')
            quit()
            continue
        print()
        sum = 0
        list_score = []
        while True:
            while True:
                try:
                    score = input(f"请输入科目 {sum+1} 的分数：")
                    if score == 'n':
                        break
                    score = float(score)
                    number = input(f"请输入科目 {sum+1} 的学分：")
                    if number == 'n':
                        break
                    number = float(number)
                except:
                    print('请输入数字！')
                else:
                    break
            if score == 'n' or number == 'n':
                quit()
                break
            list_score.append([score, number])
            sum += 1
            print('\n')
        list_stu.append(Student(name, list_score, getGPA(list_score)))
        flush()
        print('添加成功！')
        quit()
    elif op == '2':
        print()
        for stu in list_stu:
            print(stu.get_stuGPA())
        quit()
    elif op == '3':
        print()
        for stu in list_stu:
            stu.print_stu()
            print()
        quit()
    elif op == '4':
        print()
        key = input('请输入学生姓名：')
        for stu in list_stu:
            i = 0
            if key in stu.name:
                i += 1
                if i == 1:
                    print('\n查询到如下学生：\n')
                stu.print_stu()
                print()
        quit()
    else:
        print('\n输入错误！')
        quit()