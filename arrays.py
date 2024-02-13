sayilar = [100,200,300,"Merhaba",True,15.5]
#programcılar saymaya sıfırdan başlar
print(sayilar[0]) 
print(sayilar)

sayilar.append(400)
print(sayilar)

sayilar.remove("Merhaba") #değere göre siler
print(sayilar)

sayilar.pop(2) #indexe göre siler (default son index)
print(sayilar)

add = [700,800,900]
sayilar.extend(add)
print(sayilar)

sayilar.clear() #listenin içini boşaltıyoruz
print(sayilar)