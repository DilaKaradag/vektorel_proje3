import googletrans 
import os
import language

language_dict = googletrans.LANGUAGES
print("Supported Languages:", language_dict)

translator = googletrans()
print("Kelime giriniz: ")
while 1<2:
    kelime = input()
    kelimesayisi = kelime.split()
    for x in range(len(kelimesayisi)):
        ceviri= googletrans.translate(kelimesayisi[x])

        print(ceviri, end=" ")
    print(" \n")
    print("Kelime giriniz: ")