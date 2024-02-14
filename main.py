print("Merhaba Tobeto")

#degiskenler 
#metinsel - numerik - obje 

text = "Hello"
kullaniciAdi = "irem"
print(text+kullaniciAdi)

studentCount = "45" #string
print(studentCount +"5") #455

studentCount = 5 #integer=> tam sayı
print(studentCount + 5)

averagePoint = 25.5 # double- decimal - float => ondalıklı sayılar
print(averagePoint + 5)

isVerified = True  # boolean 
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))

#matematiksel - mantıksal
number = 10
print(10 + 10)
print(number+ number)

print(number - 5)

print(number / 2)

print(number * 3)

print(number % 3) 
#mod:sol taraftaki değerin sağ taraftaki 
#değere bölümünden kalan sonuç 

#mantıksal operatörler => karşılaştırma operatörler

print(number == 10) #true
print(number ==11 ) #false

print(number != 10 ) #false
print(number != 11) #true

print(number > 10) #false
print(number >= 10) #true

print(number < 10) #false
print(number <= 10) #true

#string interpolation => metin birleştirme
text = "Hello"
kullaniciAdi = "irem"
totalText = text+" "+kullaniciAdi
print(totalText)

totalText = "{message} Sayın {name}".format(message="Hello",name=kullaniciAdi)
print(totalText)

#f-string 
totalText = f"Hoşgeldiniz {kullaniciAdi}"
print(type(totalText))