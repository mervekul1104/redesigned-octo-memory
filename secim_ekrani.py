import tkinter as tk
from PIL import Image, ImageTk  # pillow kütüphanesi gerekiyor

def hata_ayikla():
    print("Hata ayıklama sayfasına gidiliyor...")

def kod_iyilestir():
    print("Kod iyileştirme sayfasına gidiliyor...")

# Pencereyi oluştur
pencere = tk.Tk()
pencere.title("İşlem Seçimi")
pencere.geometry("600x400")  # pencere boyutunu isteğe göre ayarla

# Arkaplan resmini yükle
arkaplan_resmi = Image.open("arkaplan.png")  # görselin adı aynı olmalı
arkaplan_resmi = arkaplan_resmi.resize((600, 400))  # pencereye göre boyutlandır
arkaplan_foto = ImageTk.PhotoImage(arkaplan_resmi)

# Canvas üzerinde arkaplan resmi göster
canvas = tk.Canvas(pencere, width=600, height=400)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=arkaplan_foto, anchor="nw")

# Butonları canvas üzerine yerleştir
buton1 = tk.Button(pencere, text="Hataları Ayıkla", width=20, command=hata_ayikla)
buton2 = tk.Button(pencere, text="Kodu İyileştir", width=20, command=kod_iyilestir)

buton1_window = canvas.create_window(200, 150, anchor="nw", window=buton1)
buton2_window = canvas.create_window(200, 200, anchor="nw", window=buton2)

pencere.mainloop()
