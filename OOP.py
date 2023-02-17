# class Point:
#     def __init__(self,x=0,y=0):
#         self.__x = self.__y = 0
#         if self.__check_val(x) and self.__check_val(y):
#             self.__x = x
#             self.__y = y
#     @classmethod
#     def __check_val(cls, x):
#         return type(x) in (int, float)
#
#     def set_coord(self, x,y):
#         if self.__check_val(x) and self.__check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             raise ValueError("Координаты должны быть числами")
#     def get_coord(self):
#         return self.__x , self.__y
#
# pt = Point(1,2)
# pt.set_coord(34,6)
#
# print(pt.get_coord())
# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def set_coord(self, x, y):
#         if self.MIN_COORD <= x <= self.MAX_COORD:
#             self.x = x
#             self.y = y
#
#     @classmethod
#     def set_bound(cls, left):
#         cls.MIN_COORD = left
#     def __getattribute__(self, item):
#         if item == "x":
#             raise ValueError("Доступ запрещён")
#         else:
#             return object.__getattribute__(self, item)
#     def __setattr__(self, key, value):
#         if key == "z":
#             raise AttributeError("Недопустимое имя атрибута")
#         else:
#             object.__setattr__(self, key, value)
#             # self.__dict__[key] = value так можно но не рекомендуется
#     def __getattr__(self, item):
#         return False
#     def __delattr__(self, item):
#         print("__delattr__: " + item)
#         object.__delattr__(self, item)


# pt1 = Point(1, 2)
# pt2 = Point(10, 20)
# print(pt1.MAX_COORD)
# pt1.set_bound(-100)
# print(pt1.__dict__)
# print(Point.MIN_COORD)
# a = pt1.y
# print(a)
# pt1.z = 5
# print(pt1.yy)
# del pt1.x
# print(pt1.__dict__)

# class ThreadData:
#     __shared_attrs = {
#         'name':'thread1',
#         'data': {},
#         'id':1
#
#     }
#     def __init__(self):
#         self.__dict__ = self.__shared_attrs
# th1 = ThreadData()
# print(id(th1.__dict__))
# th2 = ThreadData()
# print(id(th2.__dict__))
# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def old(self):
#         return self.__old
#
#     def get_name(self):
#         return self.__name
#
#     @old.setter
#     def old(self, old):
#         self.__old = old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#     def set_name(self, name):
#         self.__name = name
#     # old = property(get_old, set_old)
#     # old = property()
#     # old = old.setter(set_old)
#     # old = old.getter(get_old)
#
#
# p = Person('Сергей', 20)
# del p.old
#
# print( p.__dict__)
from string import ascii_letters


class Person:
    __S_RUS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя-"
    __S_RUS_UPPER = __S_RUS.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        

        self.__fio = fio
        self.old = old
        self.ps = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("Фио должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат данных")
        letters = ascii_letters + cls.__S_RUS + cls.__S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно испорльховать только буквенные символы и дефис")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом в диапозоне от 14 до 120")

    @classmethod
    def verify_weight(cls, weight):
        if type(weight) != float or weight < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше")

    @classmethod
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть строкой")
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")
        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def ps(self):
        return self.__ps

    @ps.setter
    def ps(self, ps):
        self.verify_ps(ps)
        self.__ps = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight


p = Person("Макаров Андрей Вячеславович", 16, "1234 567890", 60.2)
p.weight = 34.5
p.old = 18
p.ps = '2452 209123'
print(p.weight, p.old, p.ps, p.fio)
print(p.__dict__)

