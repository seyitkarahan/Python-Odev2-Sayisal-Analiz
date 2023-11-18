
# [2,4]
alt_sinir = 2
ust_sinir = 4
sayac = 0

def f(x):
    return x**3 - 2*x**2 - 5

while sayac < 4:
    islem = (alt_sinir + ust_sinir) / 2

    if f(islem) == 0:
        break
    elif f(islem) * f(alt_sinir) < 0:
        ust_sinir = islem
    else:
        alt_sinir = islem

    print((sayac + 1), ". Kök: ", islem)

    sayac += 1
