# 生成随机密码案例
import string
import random
names = ['afjk','fjds','sdjk','oejf','lisr']
f = open('password.txt', 'w')
pass_str = string.ascii_letters + string.digits #+ string.punctuation #ascii_letters:所有大小写字母、digits:所有数字、punctuation:特殊符号
for i in names:
    passwd = ''.join(random.sample(pass_str, 10)) #join函数，以前面的字符为分隔符，将后面的字符串列表拼接成一个字符串  sample函数，用于从参数1序列、集合中选取参数2个无重复元素
    # f.write(i + ': ' + passwd + '\n')
    f.write(f'{i}: {passwd}\n') #与上式等价
f.close()
print('密码生成完毕!')