a = [1,2,3,4]
b = [3,4,5,6,7,8]
c = "python"
z = zip(a,b,c)
print(z)
lz = list(z)
print(lz)
t1,t2,t3 = zip(*lz)
print(*lz)
print(t1,t2,t3, sep="\n")




# def get_list():
#     for x in range(1,10):
#         a = range(x,11)
#         yield sum(a)/len(a)
#
# w = get_list()
# print(list(w))
# a = (x**2 for x in range(6))
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# b = list(a)
# print(b)





# import pickle
# try:
#     with open("out.bin", "rb") as file:
#         b1 = pickle.load(file)
#         b2 = pickle.load(file)
#         b3 = pickle.load(file)
#         b4 = pickle.load(file)
# except:
#     print("Ошибка при работе с файлом")
# print(b1,b2,b3,b4, sep="\n")
# import pickle
# book1 = [("Евгений Онегин", "Пушкин А.С.", 200)]
# book2 = [("Муму", "Тургенев И.С.", 250)]
# book3 = [("Мастер и Маргарита", "Булгаков М.А.", 500)]
# book4 = [("Мёртвые души", "Гоголь Н.В.", 190)]
#
# try:
#     with open("out.bin", "wb") as file:
#         pickle.dump(book1, file)
#         pickle.dump(book2, file)
#         pickle.dump(book3, file)
#         pickle.dump(book4, file)
# except:
#     print("Ошибка при работе с файлом")

# import pickle
# books = [("Евгений Онегин", "Пушкин А.С.", 200),
#          ("Муму", "Тургенев И.С.", 250),
#          ("Мастер и Маргарита", "Булгаков М.А.", 500),
#          ("Мёртвые души", "Гоголь Н.В.", 190)]
# чтение из бинарного файла
# file = open("out.bin", "rb")
# bs = pickle.load(file)
# file.close()
# print(bs)

# запись (бинарная) в файл
# file = open("out.bin", "wb")
# pickle.dump(books, file)
# file.close()


# запись в файл
# try:
#     with open("out.txt", "a+") as file:
#         file.seek(0)
#         file.writelines(["werty\n", "cucumber\n"])
#         s = file.readlines()
#         print(s)
#
# except:
#     print("Ошибка при работе с файлом")
#
#Чтение из файла
#
# try:
#     # file = open("myfile.txt", encoding="utf-8")
#     with open("myfile.txt", encoding="utf-8") as file:
#         s = file.readlines()
#         int(s)
#         print(s)
#     # try:
#     #     s = file.readlines()
#     #     int(s)
#     #     print(s)
#     # finally:
#     #     print("File is close")
#     #     file.close()
# except FileNotFoundError:
#     print("Не возможно открыть файл")
# except:
#     print("ошибка при работе с файлом")
# finally:
#     print(file.closed)

