ortalamaNot = float(input("lütfen ortalamanizi giriniz: "))

print(type(ortalamaNot))

if ortalamaNot >50:
    print("Başarılı")
    if ortalamaNot >80:
        print("Bravo!!!")
#else if = elif
elif ortalamaNot >40:
    print("Ortalama")
else:
    print("Dersten kaldınız")

print("if bloğundan bağımsız bir kısım")

# if ortalamaNot >50 and ortalamaNot <70:
#     print("Başarılı")
# else:
#     print("Dersten kaldınız")

# print("if bloğundan bağımsız bir kısım")

