# # d = {"house":"дом",
# #      "car":"машина",
# #      "tree":"дерево",
# #      "road":"дорога",
# #      "river":"река",}
# # print(d)
# # print(d["house"])
# # print(d["car"])
# # a = dict(one =1, two = 2)
# # print(a)
# lst = [[2,"плохо"],[3,"удовлетворительно"],[4,"хорошо"]]
# a = dict(lst)
# print(a)
# a[True] = "истина"
# a[False] = "ложь"
# a[3] = 34
# print(a)
# print(len(a))
# del a[2]
# print(a)
# print("bjsadj" in a)
# a[34] = 3
# print(a)
# lst = ["+6","+5","+4","+3","+2","+1"]
# a = dict.fromkeys(lst, "код страны")
# print(a)
# # a.clear()
# # print(a)
# a2 = a.copy()
# print(a2)
# a2["password"] = "werty"
# print(a2.get("+3"))
# print(a2)
# print(a2.get("pasword", "not find"))
# print(a2.setdefault("password", "pass"))
# print(a2)
# print(a2.setdefault("word", "pass"))
# print(a2)
# a2.pop("+2")
# a2.pop("+3")
# a2.pop("+4")
# a2.pop("+5")
# a2.pop("+6")
# q = a2.pop("+7", False)
# print(f"ERROR - {q}")
# print(a2)
# a = dict(a2)
# print(a)
# print(f"a - {id(a)}\na2 - {id(a2)}")
a = {'+1': 'код страны', 'password': 'werty', 'word': 'pass'}
a[3] = "three"
a["competion"] = "соревнование"
b = {'one': 1, 'two': 2, 'three': 3}
# a.popitem()
# print(a)
# a.popitem()
c = {**a, **b}
a.update(b)
print(a.keys())
print(a.values())
print(a)
print(c)
