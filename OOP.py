# class Point:
#
#     color: str= "red"
#     circle: int =2
# a = Point()
# a.color = "green"
# a.circle = 5
# print(a.color)
# print(a.circle)
# print(a.__dict__)
# setattr(Point, 'hah', "normal")
# setattr(Point,'call', 10)
# print(Point.__dict__)
# print(Point.call)
# attr
# # Point.cost = 200
# # print(Point.cost)
# # del Point.cost
# # print(Point.__dict__)
# def fool(*a):
#
#     for i in range(len(a)):
#         print(a[i].__dict__)
# class Point:
#     color = "red"
#     circle = 2
#
#     def __init__(self, x=0,y=0):
#
#         self.x = x
#         self.y = y
#     def __del__(self):
#
#     def set_coords(self, x,y):
#         self.x = x
#         self.y = y
#         print(f"x: {x}\ny: {y}")
#     def get_coords(self):
#         return (self.x, self.y)
#
#
# pt = Point()
#
# print(pt.__dict__)
# # pt = Point()
# # pt.set_coords(2,54)
# # print(pt.get_coords())
# # a = 9
# # b = 34
# # c = 'jkj'
# # fool(a,b,c)

# class Point:
#     color = "red"
#     circle = 2
#
#     def __init__(self, x=0,y=0):
#         print("Вызов INIT для - " + str(self))
#         self.x = x
#         self.y = y
#     def __new__(cls, *args, **kwargs):
#         print("Вызов NEW для - " + str(cls))
#         return super().__new__(cls)
#
# pt = Point(1,2)
# print(pt)
# class DataBase:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#
#         if cls.__instance is None:
#             print("NEW созданние")
#             print(super().__new__(cls))
#             cls.__instance = super().__new__(cls)
#         print("NEW")
#         return cls.__instance
#     def __del__(self):
#         print("DEL")
#         DataBase.__instance = None
#     def __init__(self, user, psw, port):
#         print("INIT")
#         self.user = user
#         self.psw = psw
#         self.port = port
#     def connect(self):
#         print(f"соединение с BD: {self.user}, {self.psw}, {self.port}")
#     def close(self):
#         print("Закрытие соединения с БД")
#     def read(self):
#         return "данные из БД"
#     def write(self, data):
#         print(f"Запись в БД: {data}")
#
#
# db = DataBase("root", '1234', 37)
# db2 = DataBase("admin", '5678', 21)
# print(id(db), id(db2))

class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y
    @staticmethod
    def norm2(x,y):
        return x*x+y*y


v = Vector(1, 22)
print(Vector.norm2(4,5))
res = v.get_coord()
print(res)
