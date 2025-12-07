#1-misol
rang = input("Chiroq rangini kirit: ")

if rang == "Qizil":
    print("To'xtang!")
elif rang == "Sariq":
    print("Tayyorlaning! ")
elif rang == "Yashil":
    print("Yuring!")
else:
    print("Bunday rang yo'q! ")

#2-misol
m = int(input("Internet tezligini kirit: "))
if m >= 100:
    print("Sizda ajoyib tezlik! ")
elif m >= 50 and m <= 100:
    print("Tezlik yaxshi, lekin yaxshilash mumkin!")
elif m >= 10 and m <= 50:
    print("Tezlik past!, provayder bilan bog'laning!")
elif m <= 10:
    print("Bu tezlik bn internet ishlatib bo'lmaydi!")

#3-misol
ball = int(input("Imtihon ballini kirit: "))

if ball >= 90:
    print("'A'lo")
elif ball >= 75 and ball <= 89:
    print("Yaxshi!")
elif ball >= 50 and ball <= 74:
    print("Qo'niqarli")
elif ball >= 50:
    print("Yiqildingiz!")
