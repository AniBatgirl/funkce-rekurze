import random


def vypocti_plochu(a, b=0):
    if b == 0:
        return a * a
    else:
        return a * b


print(vypocti_plochu(4, 20))
print(vypocti_plochu(a=4, b=20))


def fib_postoupnost(n):
    if n == 1 or n == 0:
        return n
    else:
        return fib_postoupnost(n - 1) + fib_postoupnost(n - 2)


# print(fib_postoupnost(18))

# for i in range(100):
#    print(fib_postoupnost(i))

# prima a nepriima rekurze, prima kdyz vola sama sebe, neprima kdyz vola jinou funkci
# obe zasiraj pamet, neprima je vic nebezpecna
# kdyz program vola sam sebe tak se v tom kroku pozastavuje a nevypne se dokud se neskonci ta funkce ktera ho zavolala
# def secti(*numbers, limit=10):


gameloop = True

while gameloop:

    tah_hrace = input("(K)amen" + "(N)uzky" + "(P)apir")
    tah_hrace = tah_hrace.lower()[0]

    tah_pocitace = random.choice(["k", "n", "p"])

    if tah_hrace == "k":
        if tah_pocitace == "k":
            print("Remiza", "hrac", tah_hrace, "pocitac", tah_pocitace)
        elif tah_pocitace == "n":
            print("vyhra", "hrac", tah_hrace, "pocitac", tah_pocitace)
        elif tah_pocitace == "p":
            print("prohra", "hrac", tah_hrace, "pocitac", tah_pocitace)
    elif tah_hrace == "n":
        if tah_pocitace == "n":
            print("Remiza", "hrac", tah_hrace, "pocitac", tah_pocitace)
        elif tah_pocitace == "p":
            print("vyhra", "hrac", tah_hrace, "pocitac", tah_pocitace)
        elif tah_pocitace == "k":
            print("prohra", "hrac", tah_hrace, "pocitac", tah_pocitace)
    elif tah_hrace == "p":
        if tah_pocitace == "p":
            print("Remiza", "hrac", tah_hrace, "pocitac", tah_pocitace)
        elif tah_pocitace == "k":
            print("vyhra", "hrac", tah_hrace, "pocitac", tah_pocitace)
        elif tah_pocitace == "n":
            print("prohra", "hrac", tah_hrace, "pocitac", tah_pocitace)
