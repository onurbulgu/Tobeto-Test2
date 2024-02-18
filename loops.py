for i in range(0,10,2):
    print(i)

#start : Döngü kaç sayısından başlasın (default 0 dan başlar şart verilmezse)
#stop : Döngü kaç kere tekrar etsin 
#step : Döngü kaç kaç arttırılsın (default 1)
    
#   -------------------------------
# kullanıcının vereceği üst limit ile alt limitten bu 
# üst limite kadar olan tüm çift sayıları ekrana yazdıralım 

# altLimit = int(input("Lütfen bir alt limit sayısı belirleyiniz: "))
# üstLimit = int(input("Lütfen bir üst limit sayısı belirleyiniz: "))
    
# # Alt ve üst limit arasındaki çift sayıları yazdır
# print(f"{altLimit} ile {üstLimit} arasındaki çift sayılar:")
# for i in range(altLimit, üstLimit + 1):
#     if i % 2 == 0:
#         print(i)
 #------------------------------------------------------
#kullanıcının girdiği sayılar arasındaki en büyüğünü bulan program yazınız

# biggestValue = 0

# for i in range(5):
#     sayi = int(input(f"{i+1}. sayiyi giriniz"))
#     if sayi > biggestValue:
#         biggestValue = sayi

# print(f"Girdiğiniz sayilar arasinda en büyük olani: {biggestValue}")
    
# sayilar =[]
# for i in range(5):
#     sayilar.append(int(input(f"{i+1}. sayiyi giriniz: ")))

# sayilar.sort(reverse=True) #desc oldu normalde orjinali asc dir.
# print(sayilar[0])
# print(min(sayilar))
# print(max(sayilar))
    
students = ["Ahmet","Tuba","Abdullah","Onur","Dilara"]
#length = uzunluk
print(len(students))
#break : ilgili döngünün o anda kırılmasını sağlar
for i in range (len(students)):
    if i>2:
        break
    print(f"{i+1}. Öğrenci:{students[1]}")
# continue : iterasyondaki current değeri atla bir sonraki değer ile devam et (görmezden gelmesini istediğimiz içeriği yazıp atlamasını sağlıyoruz)
for i in students:
    if i =="Tuba":
        continue
    print(f"Öğrenci: {i}")

i=0
while i<10:
    print("Merhaba")
    i= i+2