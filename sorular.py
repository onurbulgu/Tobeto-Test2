#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

bmi_calculation = float(question_weight / (question_height * question_height))

if bmi_calculation <= 18.5:
 print(f"Your BMI is {bmi_calculation}, you are underweight.")
elif 18.5 <= bmi_calculation < 25:
 print(f"Your BMI is {bmi_calculation}, you have a normal weight.")
elif 25 <= bmi_calculation < 30:
print(f"Your BMI is {bmi_calculation}, you are slightly overweight.")
elif 30 <= bmi_calculation < 35:
 print(f"Your BMI is {bmi_calculation}, you are obese.")
else:
  print(f"Your BMI is {bmi_calculation}, you are clinically obese.")


#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.


maas = float(input("maasınızı giriniz: "))
zamorani = float(input("zam oranını giriniz: "))

zammiktari= (maas*( zamorani / 100))
net_maas=(maas+zammiktari)
print(net_maas)


#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.



# Get the three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the largest number
#largest = max(num1, num2, num3)
largest = num1
if num2 > largest:
    largest = num2
if num3 > largest:
    largest = num3 
# Print the largest number
print("The largest number is:", largest)






#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)


import math

def calculate_area(radius):

    area = math.pi * (radius ** 2)
    return area

def calculate_perimeter(radius):
 
    perimeter = 2 * math.pi * radius
    return perimeter

radius = float(input("Enter the radius of the circle: "))


area = calculate_area(radius)
perimeter = calculate_perimeter(radius)


print("The area of the circle is:", area)
print("The perimeter of the circle is:", perimeter)


# 5.Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

# Kullanıcıdan bir sayı alınır
number = input("Enter a number: ")

# Sayıyı ters çevirir
reverse_number = number[::-1]

# Palindrom olup olmadığını kontrol eder
if number == reverse_number:
    print("The entered number is a palindrome.")
else:
    print("The number entered is not a palindrome.") 
    
