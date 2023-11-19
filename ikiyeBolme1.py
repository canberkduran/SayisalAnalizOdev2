
def f(x):
    return x**3 - 2*x**2 - 5

def ikiyeBolme(xilk,xson, iterasyonSayisi):
    if f(xilk) * f(xson) > 0:
        print("Belirtilen aralikta kök yok.")
        return None

    for _ in range(iterasyonSayisi):
        kok = (xilk + xson) / 2
        if f(kok) *f(xilk)<0:
            xson =kok
        else:
            xilk =kok

    return (xilk +xson) / 2

xilk =2
xson =4
iterasyonSayisi=4

sonuc = ikiyeBolme(xilk, xson, iterasyonSayisi)

if sonuc is not None:
    print(f"Bulunan kök: {sonuc}")
else:
    print("Kök bulunmadı.")
