def f(x):
    return x**3 + 4*x**2 - 10

def ikiyeBolme(xilk, xson, hataPayi):
    if f(xilk) * f(xson) > 0:
        print("Belirtilen aralikta kök yok.")
        return None

    iterasyon = 1
    while (xson - xilk)/2 >hataPayi:
        xkok = (xilk + xson)/2
        if f(xkok)* f(xilk) < 0:
            xson = xkok
        else:
            xilk = xkok
        iterasyon=iterasyon+1

    kok = (xilk + xson) / 2
    print(f"çözüm: {kok}")
    print(f"iterasyon sayisi: {iterasyon}")

    return kok

xilk = 1
xson = 2
hataPayi = 1e-6 # 1e-6=10^-6
sonuc = ikiyeBolme(xilk, xson, hataPayi)
