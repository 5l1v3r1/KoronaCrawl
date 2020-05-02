#!/usr/bin/env python
#! -*- coding: utf-8 -*-

#-------------------------------#
from PyQt5.QtCore import *      #
from PyQt5.QtGui import *       #
from PyQt5.QtWidgets import *   #
import sys                      #
#-------------------------------#
import qdarkstyle               #
import qdarkgraystyle           #
#-------------------------------#
import requests
from bs4 import BeautifulSoup
#-------------------------------#

class AnaSayfa(QMainWindow):
    def __init__(self):
        super().__init__()
        #---------------------------#
        self.show()
        self.setWindowTitle("Corona Virus Sayaacı - @KekikAkademi")
        self.setWindowIcon(QIcon("img/udemy.png"))
        self.setMinimumSize(QSize(500, 500))
        self.setMaximumSize(QSize(500, 500))
        self.setStyleSheet(open("style/style.qss", "r").read())
        #self.setStyleSheet(qdarkgraystyle.load_stylesheet())
        #self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        #---------------------------#
        self.TumEkran()             # TumEkran'ı Çağırdık
        self.Malzeme()              # Malzeme'yi Çağırdık

    def TumEkran(self):
        menuBar = self.menuBar()

        ### Temalar
        tema = menuBar.addMenu("Tema Değiştir")         # "menuBar" değişkenimizde menü oluşturduk

        mavimsi_tema = QAction("Mavimsi Tema", self)    # Aksiyon Belirledik
        mavimsi_tema.setShortcut("ALT+1")               # Kısa Yol Tuşu

        kara_tema = QAction("Kara Tema", self)          # Aksiyon Belirledik
        kara_tema.setShortcut("ALT+2")                  # Kısa Yol Tuşu

        tema.addAction(mavimsi_tema)                    # Menümüze aksiyonu yönlendirdik
        tema.addAction(kara_tema)                       # Menümüze aksiyonu yönlendirdik

        tema.triggered.connect(self.BarTepki)           # Aksiyonlarımızı BarTepki'ye yönlendirdik

        ### Hakkında
        hakkinda = menuBar.addMenu("Hakkında")          # "menuBar" değişkenimizde menü oluşturduk
        hakkinda.addAction("Hakkında")                  # Aksiyon Belirledik
        hakkinda.triggered.connect(self.BarTepki)       # Aksiyonu BarTepki'ye yönlendirdik

    def Malzeme(self):
        malzeme = QWidget(self)

        # vBox -- Dikey Yerleşim (Vertical Layout)
        malzeme.vBox = QVBoxLayout()

        # hBox -- Yatay Yerleşim (Horizontal Layout)
        malzeme.hBox = QHBoxLayout()
        malzeme.hBox.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # Dünya
        malzeme.dunya = QToolButton()
        #dunya.setIcon("world.png")
        malzeme.dunya.setText("Dünya")
        malzeme.dunya.setToolButtonStyle(Qt.ToolButtonTextOnly)
        malzeme.dunya.setCursor(QCursor(Qt.PointingHandCursor))
        malzeme.dunya.clicked.connect(self.dunyaRakam)

        # Türkiye
        malzeme.turkiye = QToolButton()
        #malzeme.turkiye.setIcon("turkiye.png")
        malzeme.turkiye.setText("Türkiye")
        malzeme.turkiye.setToolButtonStyle(Qt.ToolButtonTextOnly)
        malzeme.turkiye.setCursor(QCursor(Qt.PointingHandCursor))
        malzeme.turkiye.clicked.connect(self.trRakam)

        malzeme.SonGuncelleme = QLabel(f"Son Guncelleme saat | tarih")
        malzeme.SonGuncelleme.setAlignment(Qt.AlignHCenter)

        # Yatay Düzen'e(hBox'a) Yerleştir
        malzeme.hBox.addWidget(malzeme.dunya)
        #malzeme.hBox.addStretch()         # Dikey dinamik uzaklığı koru
        malzeme.hBox.addWidget(malzeme.turkiye)

        # Dikey Düzen'e(vBox'a) Yerleştir
        malzeme.vBox.addLayout(malzeme.hBox)
        malzeme.vBox.addWidget(malzeme.SonGuncelleme)
        #------------------------------------------------------------------------#
        malzeme.setLayout(malzeme.vBox)
        self.setCentralWidget(malzeme)  ## https://stackoverflow.com/a/37306238
        #------------------------------------------------------------------------#

    def BarTepki(self,action):
        ### Temalar
        if action.text() == "Mavimsi Tema":
            self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
        if action.text() == "Kara Tema":
            self.setStyleSheet(qdarkgraystyle.load_stylesheet())

        ### Hakkında
        if action.text() == "Hakkında":
            self.hakkinda_pencere = QWidget()
            self.hakkinda_pencere.show()
            self.hakkinda_pencere.setWindowTitle(f"{action.text()} / {self.windowTitle()}")
            self.hakkinda_pencere.setWindowIcon(QIcon("img/udemy.png"))
            self.hakkinda_pencere.setStyleSheet(open("style/style.qss", "r").read())

            self.vBox = QVBoxLayout()

            # Logo
            self.logo = QLabel()
            self.logo.setPixmap(QPixmap(r"img/KekikAkademiQt5Logo.png"))
            self.logo.setAlignment(Qt.AlignCenter)

            # Açıklama
            self.aciklama = QLabel()
            self.aciklama.setText("""@keyiflerolsun tarafından Eğitim Amaçlı Yazılmıştır.
            Telegram Kanalımıza Bekleriz: @KekikAkademi""")
            self.aciklama.setFont(QFont("Courier", 16, QFont.Bold))
            self.aciklama.setAlignment(Qt.AlignTop | Qt.AlignCenter)

            self.vBox.addWidget(self.aciklama)
            self.vBox.addWidget(self.logo)

            self.hakkinda_pencere.setLayout(self.vBox)
        #----------------------------------------------------------------------------------------------------------------#

    def dunyaRakam(self):
        pass

    def trRakam(self):
        pass

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)           # Uygulamamızı Oluşturduk
    pencere = AnaSayfa()                        # Penceremizi Oluşturkuk
    sys.exit(uygulama.exec())                   # Çıkış yapıldığı zaman, uygulamayı kapat