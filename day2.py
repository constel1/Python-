# words = [-23,2,-5,78,45,3,-75,4]
# print(words)
#
# for i, d in enumerate(words):
#     if 9<abs(d) <100:
#         words[i] = 0
# print(words)
t = ["a","b","v","g","d","e","zh","z","i","y",
     "k","l","m","n","o","p","r","s","t","u",
     "f","h","c","ch","sh","shch","","y","","e","yu","ya"]

start = ord("а")
title = "Программирование на Python - это норма"
sus = ""
for s in title.lower():
    if "а"<= s <= "я":
        
        sus+= t[ord(s) - start]

    elif s == "ё":
        sus+= "yo"
    elif s in " !&?;:.,":
        sus+= "-"
    else:
        sus+=s
while sus.count("--"):
    sus = sus.replace("--", "-")
print(sus)