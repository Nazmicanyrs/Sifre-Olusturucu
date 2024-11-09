import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QFrame,QCheckBox,QLineEdit
from PyQt5.QtGui import QIcon
from random import *

import string
app = QApplication(sys.argv)
pencere = QMainWindow()
pencere.setWindowTitle("Şifre Oluşturucu")
pencere.setGeometry(600, 600, 600, 600)

sifre_buyuk = [string.ascii_uppercase]
sifre_kucuk = [string.ascii_lowercase]
sifre_sayi = [string.digits]
sifre_sembol = [string.punctuation]

sayac = 0
sifre2 = list()
def kontrol(sayac):
    # Sıfırlama işlemi
    sifre2.clear()  # Her butona basıldığında önceki şifreyi temizle

    if karakter_sayisi.text() == "":
        uyarı.setText("Lütfen Karakter Sayısını Giriniz")
    else:
        donustur = int(karakter_sayisi.text())
        
        # En az bir karakter türü seçildiğinden emin ol
        if secim.isChecked():
            sifre2.append(sifre_buyuk[0][randint(0, 25)])
        if secim2.isChecked():
            sifre2.append(sifre_kucuk[0][randint(0, 25)])
        if secim3.isChecked():
            sifre2.append(sifre_sayi[0][randint(0, 9)])
        if secim4.isChecked():
            sifre2.append(sifre_sembol[0][randint(0, len(sifre_sembol[0]) - 1)])
        
        # Kalan karakterleri rastgele seç
        while len(sifre2) < donustur:  # Şifre uzunluğu hedefe ulaşana kadar devam et
            rast = randint(0, 3)  # 0-3 arasında rastgele bir sayı
            if rast == 0 and secim.isChecked():
                sifre2.append(sifre_buyuk[0][randint(0, 25)])
            elif rast == 1 and secim2.isChecked():
                sifre2.append(sifre_kucuk[0][randint(0, 25)])
            elif rast == 2 and secim3.isChecked():
                sifre2.append(sifre_sayi[0][randint(0, 9)])
            elif rast == 3 and secim4.isChecked():
                sifre2.append(sifre_sembol[0][randint(0, len(sifre_sembol[0]) - 1)])
        
        # Oluşturulan şifreyi göster
        uyarı.setWordWrap(True)
        uyarı.setMaximumWidth(999)  # Maximum width set to accommodate longer passwords
        uyarı.setText("Oluşturulan Şifre: " + ''.join(sifre2))  # Şifreyi QLabel'de göster
        uyarı.adjustSize()  # QLabel boyutunu içeriğe göre ayarla

def kopyala():
    clipboard = QApplication.clipboard()
    kopyalanan_sifre=" "
    for i in sifre2:
        kopyalanan_sifre+=i
    clipboard.setText(kopyalanan_sifre)

icon = QIcon("Sifre.png")
pencere.setWindowIcon(icon)

yazi = QLabel("Şifre Oluşturucu!", pencere)
yazi.setStyleSheet("background-color:#5cb0ff;text-align:center;padding:10px;border-radius:10px;font-size:20px;")
yazi.setWordWrap(True)

yazi.setGeometry(200, 20, 180,50)

yatay_cizgi = QFrame(pencere)
yatay_cizgi.setStyleSheet("background-color:black;height:2px;")
yatay_cizgi.setGeometry(140, 90, 300, 2)

secim = QCheckBox("A,z", pencere)
secim.setGeometry(140, 120, 150, 20)

secim2= QCheckBox("a-z", pencere)
secim2.setGeometry(140, 150, 150, 20)

secim3= QCheckBox("0-9", pencere)
secim3.setGeometry(140, 180, 150, 20)

secim4= QCheckBox("!#/*!^%&'", pencere)
secim4.setGeometry(140, 210, 150, 20)


yazi2=QLabel("Karakter Sayısı:", pencere)
yazi2.setGeometry(10, 240, 120, 40)
yazi2.setWordWrap(True)
yazi2.setStyleSheet("font-size:15px;color:black;")

karakter_sayisi = QLineEdit(pencere)
karakter_sayisi.setGeometry(110, 245, 200, 30)
karakter_sayisi.setStyleSheet("font-size:15px;color:black;")
karakter_sayisi.setPlaceholderText("Karakter Sayısını Giriniz")


sifre_olustur = QPushButton("Şifre Oluştur", pencere)
sifre_olustur.setGeometry(320, 245, 100, 30)
sifre_olustur.setStyleSheet("font-size:15px;color:black;")
sifre_olustur.clicked.connect(kontrol)


kopyala_buton = QPushButton("Kopyala", pencere)
kopyala_buton.setGeometry(430, 245, 100, 30)
kopyala_buton.setStyleSheet("font-size:15px;color:black;")
kopyala_buton.clicked.connect(kopyala)

uyarı = QLabel("", pencere)
uyarı.setGeometry(10, 350, 200, 30)
uyarı.setStyleSheet("font-size:15px;color:black;")


pencere.show()
sys.exit(app.exec_())
