def f(x):
    return x**(1/3)

def f_turev(x):
    return (x**(-2/3))/3

def newton_raphson_iterasyon(x):
    root = x - f(x) / f_turev(x)
    return root, f(x), f_turev(x)

def iterasyon_yazdir(iterasyon, root, fx, fpx):
    print(f"{iterasyon}. İterasyon - Kök f(x): {fx:.6f}, Kök f'(x): {fpx:.6f}, Kök Tahmini: {root:.6f}")
def run_newton_raphson(x0, iteration_size=4):
    root = x0

    for iterasyon in range(1, iteration_size + 1):
        root, fx, fpx = newton_raphson_iterasyon(root)
        iterasyon_yazdir(iterasyon, root, fx, fpx)

x0 = 1
iterasyon_boyut = 4
run_newton_raphson(x0, iterasyon_boyut)
