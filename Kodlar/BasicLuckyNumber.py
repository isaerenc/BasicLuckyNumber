__author__ = "isaerenc"

import random

while True:
    choices = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"]
    bilgisayar = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Bakalım 1'den 15'a kadar tutacağım o gizemli sayıyı bilebilecek misin? (Sayı lütfen 1-10 arasında olsun) Hadi gir tahminini: ").lower()
    if player == bilgisayar:
        print("Şanslı sistem", bilgisayar, "sayısını seçti.")
        print("Sen ise", player, "sayısını seçtin")
        print("Doğru Tahmin!")
    elif player < bilgisayar:
        print("Şanslı sistem", bilgisayar, "sayısını seçti.")
        print("Sen ise", player, "sayısını seçtin")
        print("Tahiminin yanlış! :(")
    elif player > bilgisayar:
        print("Şanslı sistem", bilgisayar, "sayısını seçti.")
        print("Sen ise", player, "sayısını seçtin")
        print("Tahiminin yanlış! :(")

