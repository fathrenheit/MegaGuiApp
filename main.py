
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

from utils.helper_functions import ClickableLabel

class EntryPoint(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("EntegraX")
        self.setMinimumSize(1024, 640)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_app_layout = QHBoxLayout(central_widget)
        side_menu = self.initSideMenu()
        main_app_layout.addLayout(side_menu, 2)
        
        modules = self.form_module_layout()
        main_app_layout.addLayout(modules, 8)

    def form_module_layout(self):

        main_module_layout = QVBoxLayout()
        company_logo = self.initCompanyLogo()
        
        modules_grid_layout = QGridLayout()
        eta_daily_sum = self.initEtaDailySummary()
        top_sales_info = self.initTopList()
        balance_sheet = self.initEtaBilanco()
        balance_sheet_official = self.initMikroBilanco()
        modules = [eta_daily_sum, top_sales_info, balance_sheet, balance_sheet_official]
        for ix, module in enumerate(modules):
            i = ix //2
            j = ix % 2
            modules_grid_layout.addLayout(module, i, j)
        
        main_module_layout.addLayout(company_logo)
        main_module_layout.addLayout(modules_grid_layout)
        return main_module_layout
    
    def initSideMenu(self):
        side_menu_layout = QVBoxLayout()
        modules = [
            'ALIŞ FATURALARI İÇİN ŞABLON OLUŞTUR',
            'BİLANÇO ANALİZİ',
            'CARİ ANALİZİ',
            'SATIŞ FATURALARI',
            'STOK FİYAT GÜNCELLEME',
            'STOK HAREKET ANALİZİ',
            'TAHSİLÂT MAKBUZU ARŞİV OLUŞTUR',
            'TAHSİLÂT MAKBUZU GİRİŞİ',

        ]
        for module in modules:
            label = ClickableLabel(module)
            side_menu_layout.addWidget(label)
        side_menu_layout.addStretch(20)
        return side_menu_layout

    def initCompanyLogo(self):
        header_layout = QHBoxLayout()


        label_logo = QLabel("FIRMA LOGOSU --")
        label_company_name = QLabel("SALİHPAŞAOĞLU GIDA VE İNŞAAT LTD. ŞTİ.")
        label_additional_info = QLabel("Sirket analiz programi")
        label_usd_gold = QLabel("Dolar/TL: --,--")        # optiONAL usd/ry ve gram/altin

        label_dict = {label_logo:               {'px':16, 'bold':True, 'italic':False, 'underlined':False}, 
                      label_company_name:       {'px':20, 'bold':True, 'italic':False, 'underlined':True},
                      label_additional_info:    {'px':12, 'bold':False, 'italic':True, 'underlined':False}, 
                      label_usd_gold:           {'px':12, 'bold':False, 'italic':False, 'underlined':False}}

        for label, features in label_dict.items():
            font = QFont()
            font.setFamily(u"Cascadia Code SemiBold")
            font.setPixelSize(features['px'])
            font.setBold(features['bold'])
            font.setItalic(features['italic'])
            font.setUnderline(features['underlined'])
            label.setFont(font)

        header_layout.addStretch(10)
        header_layout.addWidget(label_logo)
        header_layout.addWidget(label_company_name)
        header_layout.addWidget(label_additional_info)
        header_layout.addWidget(label_usd_gold)
        
        return header_layout
    
    def initEtaDailySummary(self):
        eta_daily_summary_layout = QVBoxLayout()
        font = QFont()
        font.setFamily(u"Cascadia Code SemiBold")
        # font.setUnderline(True)
        
        title = QLabel("ETA Günlük Hareketler:")
        # title.setFont(font)
        
        self.alislar = QLabel("Alışlar:\t---.---.---,-- [TL]")
        self.satislar = QLabel("Satışlar:\t---.---.---,-- [TL]")
        self.kar_tutar = QLabel("Kâr:\t\t---.---.---,-- [TL]")
        self.kar_yuzde = QLabel("Kârlılık:\t-- [%]")

        eta_daily_summary_layout.addWidget(title, 1)
        for label in [title, self.alislar, self.satislar, self.kar_tutar, self.kar_yuzde]:
            if label is title:
                font.setUnderline(True)
                font.setPixelSize(12)
                label.setFont(font)
                eta_daily_summary_layout.addWidget(label, 1)
                # eta_daily_summary_layout.addStretch(2)
            else:
                font.setUnderline(False)
                font.setPixelSize(10)
                label.setFont(font)
            eta_daily_summary_layout.addWidget(label, 1)
        eta_daily_summary_layout.addStretch(5)
        return eta_daily_summary_layout

    def initTopList(self):
        top_list_layout = QVBoxLayout()
        title = QLabel("Günlük Satış Özeti:")
        font = QFont()
        font.setFamily(u"Cascadia Code SemiBold")
        font.setUnderline(True)
        title.setFont(font)
        # title = QLabel("Satis ozeti")
        top_list_layout.addWidget(title,1)
        top_list_layout.addStretch(5)

        return top_list_layout
        

    def initEtaBilanco(self):
        eta_bilanco_layout = QVBoxLayout()
        title = QLabel("Güncel Bilanço:")
        font = QFont()
        font.setFamily(u"Cascadia Code SemiBold")
        font.setUnderline(True)
        title.setFont(font)
        eta_bilanco_layout.addWidget(title, 1)
        eta_bilanco_layout.addStretch(5)
        return eta_bilanco_layout
    
    def initMikroBilanco(self):
        mikro_bilanco_layout = QVBoxLayout()
        title = QLabel("Mikro Kısmî Bilanço:")
        font = QFont()
        font.setFamily(u"Cascadia Code SemiBold")
        font.setUnderline(True)
        title.setFont(font)
        mikro_bilanco_layout.addWidget(title, 1)
        mikro_bilanco_layout.addStretch(5)
        return mikro_bilanco_layout
    
"""
# Eklenecek:

1- Genel font ayari yapilacak. Cascadia semi bold standart olarak kullandigim font oldu gibi.ozellikle modullerin fontlarini ayarlarken 3 satir kodu her fonksiyonda tekrarladim.
2- Bu sayfa main değil, entry point sayfası olarak değiştirilebilir. main.py de en miiinimal düzeyde kod olması gerekiyor
3- Şirket logosu eklenecek. Sallama bir şey olabilir. Sonrasında düzeltilir. Font da aynı şekilde.
4- Modullere eklenecek verilere ait sorgular dosyalanacak.
    0. modül: şirket logosu ve güncel dolar tl değeri. view tamam gibi, controller gereksiz, model request ile webden dolar değerini çeken kod parçacığı
    1. modül: eta o gün içerisinde yapılan 
        alışlar
        satışlar
        kar tutar
        kar %

        

        son 1 haftaya ait stacked histogram grafik

    2. modül: Günlük para hareketleri:
        tahsilatlar
            - kredi kartı kasasından günlük tahsilat
            - nakit tahsilatlar
            - bankaya gönderilenler
            - alınan çekler

        ödemeler
            - nakit kasalardan ödenenler
            - bankadan gönderilen paralar
            - çekilen kredi kartları
            - ödenen çekler
        - en çok satılan ürünler (tutar)
        - en çok kar bırakan ürünler
        - zararına satılan ya da çok düşük kârla satılan ürünler
        - 
        -
        ya da 
        günlük hareket özeti:
        - günlük çekilen kart
        - bankalara gelen ve giden havaleler
        - günlük nakit tahsilatlar
        - En çok kar 
    
    3. modül: ETA Bilanço. Şirketin güncel bilanço verilerini kapsar
        - stok envanter * 1
        - stok envanter * 5
        - ortalama karlılık

        - bankalar
        - cariler
        - kasalar

        - yaklaşan kredi kartı ödemeleri
        - yaklaşan çek ödemeleri eklenebilir

    4. modül: kısmi bilanço mikro:
        - stok envanter kdvlerine göre
            - günlük giriş çıkışlar treeview olarak eklenebilir
        - bankalar
            - giriş çıkışlar treeview olarak gösterilebilir
        - pos ta biriken para


"""


if __name__ == "__main__":
    app = QApplication(sys.argv)  # Initialize the application
    window = EntryPoint()  # Create an instance of MyApp
    window.show()  # Show the main window
    sys.exit(app.exec())  # Start the event loop

"""
1. modul
ETA Gunluk hareketler:
    ALISLAR
    SATISLAR
    KAR
    KARLILIK

2. modul

3. modul
ETA BILANCO
    - stok envanter
    - bankalar
        - ziraat
            + gelen
            - giden
        - denizbank
            + gelen
            - giden
        - akbank
            + gelen
            - giden
    - cariler
        - alacaklilar
        - borclular
+++++++++++++TOPLAM ++++++++++

    - Z ve K kasa
        - Gunluk pos Z
        - Gunluk pos K

    -
        
4. modul
MIKRO VERILER
    - stok envanter
        - %1: 
            - girisler
            - cikislar
        - %10
            - girisler
            - cikislar
        - %20
            - girisler
            - cikislar
        
        - Bankalar

"""
