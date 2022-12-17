# a = int(input("vvedite pervoe chislo"))
# b = int(input("vvedite vtoroe chislo"))
# print (a+b)
#
# a = int(input("vvedite pervoe chislo"))
# b = int(input("vvedite vtoroe chislo"))
# print (a+b)


# a = (input("vvedite pervoe chislo"))
# b = (input("vvedite vtoroe chislo"))
# print (a+b)

            #калькулятор(2 числ и сама операция)

perv = int(input("первое число:"))
vtor = int(input("второе число:"))
znak = (input("знак:"))
def calc(perv,vtor,znak):
    if znak =="+":
        return (perv+vtor)
    if znak == "-":
        return (perv-vtor)
    if znak == "*":
        return (perv*vtor)
    if znak == "/":
        return (perv/vtor)
print ("итог =", calc(perv,vtor,znak))



