# property:
# 把一个方法当成一个属性使用
# 这个方法一定有返回值


# 年龄异常
class AgeError(Exception):
    def __init__(self, error_age):
        Exception.__init__(self)
        self.error_age = error_age

    def __str__(self):
        return f'年龄数值（{self.error_age}）错误，应该在 1 - 150 之间！'


# 人类
class Person:
    def __init__(self):
        self.__age = None

    # @property
    # def age(self):
    #     return self.__age
    #
    # @age.setter
    # def age(self, new_age):
    #     if new_age < 0 or new_age > 150:
    #         raise AgeError(new_age)
    #     else:
    #         self.__age = new_age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age < 0 or new_age > 150:
            raise AgeError(new_age)
        else:
            self.__age = new_age

    age = property(get_age, set_age)


if __name__ == '__main__':
    person = Person()
    try:
        person.age = 151  # person.set_age()
    except Exception as e:
        print(e)
    else:
        print(person.age)  # person.get_age()
