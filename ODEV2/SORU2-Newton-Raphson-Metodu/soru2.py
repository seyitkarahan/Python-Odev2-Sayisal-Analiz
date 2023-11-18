e = 2.7182818284

def f(x):
    return 4 * e**(-0.5 * x) - x

def df(x):
    return -2 * e**(-0.5 * x) - 1

# Başlangıç değeri
x0 = 2
sayac = 0

while sayac < 4:
    x1 = x0 - f(x0) / df(x0)
    print((sayac + 1), ". Kök: ", x1)
    x0 = x1
    sayac += 1
