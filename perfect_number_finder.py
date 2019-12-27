import numpy as np   #liste islemleri icin gereken kutuphane
np.set_printoptions(suppress=True) # numpy normalde büyük sayilar icin bilimsel yaziyor / 8.128e03 seklinde bunu onlemek icin ayar

numbers = [] # yedeklenecek sayilar icin dizi olusturuldu.
counter = 2 # sayac icin sayı olusturuldu ilk 2 degeri alindi.
number_of_number = 4 # kac tane sayı bulmak istedigimizi yaziyoruz

def bolen_bul(number):
    bolenler = [] #bölenleri yedeklemek icin liste.
    for i in range(1,(int(number/2)+1)): #sayinin yarisina kadar bakiyoruz.
        if ((number%i) == 0):
            bolenler = np.append(bolenler,i) # buldugumuz sayilari diziye ekliyoruz.
    return bolenler


while(len(numbers) != number_of_number): # istedigimiz sayida sayi bulana kadar devam edecek
    if(np.sum(bolen_bul(counter))==counter): # buldugumuz sayilarin toplamı bastaki sayiyla kiyaslandi
        numbers = np.append(numbers,counter) #sayi diziye eklendi
    counter = counter + 1
print(numbers)
