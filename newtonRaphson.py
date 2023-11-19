e = 2.71
def fonksiyon(x):
    return 4 * (e**(-0.5 * x)) - x

def turev(x):
    return -0.5 * 4 * e**(-0.5 * x) - 1

def newtonRaphson(x,iterasyon):
    for i in range(iterasyon):
        x = x -fonksiyon(x) /turev(x)
    return x, i+1

x = 2

iterasyon = 4

kok,iterasyonSayisi = newtonRaphson(x,iterasyon)

print(f"Bulunan kök:{kok}")
print(f"Iterasyon sayisii:{iterasyonSayisi}")
