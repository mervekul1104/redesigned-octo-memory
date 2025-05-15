import subprocess
import tkinter as tk
from tkinter import Label, Frame, Text
from PIL import Image, ImageTk
import sys

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Misafir"


def kodu_iyilestir():
    kod_kutusu.delete("1.0", tk.END)  # Önce temizle
    iyilestirilmis_kod = """def toplama(a, b):
    return a + b"""
    kod_kutusu.insert(tk.END, iyilestirilmis_kod)

def geri_don():
    panel.destroy()  # Bu pencereyi kapat
    subprocess.run(["python", "main.py",username])

# Ana panel
panel = tk.Tk()
panel.title("İyileştirme")
panel.geometry("1280x720")
panel.configure(bg="#000428")

# Arka plan resmi
background_image = Image.open("background.png")
background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(background_image)
bg_label = Label(panel, image=bg_photo)  # ← DÜZELTME: tk değil, pencere olmalı
bg_label.image = bg_photo  # referans tutulmalı
bg_label.place(relwidth=1, relheight=1)

# Başlık
baslik = Label(panel, text="İYİLEŞTİRME", font=("Georgia", 30, "bold"),
               fg="white", bg="#000428")
baslik.pack(pady=(30, 10))

# Alt çizgi
cizgi = Frame(panel, bg="white", height=2, width=300)
cizgi.pack(pady=5)

# Kod kutusu
kod_kutusu = Text(panel, bg="black", fg="lime", width=108, height=22,
                  font=("Courier New", 12))
kod_kutusu.pack(pady=40)

# Buton
buton = tk.Button(panel, text="İYİLEŞTİR   ➤", font=("Georgia", 14, "bold"),
                  bg="white", fg="#000428", padx=30, pady=10, borderwidth=2,
                  command=kodu_iyilestir)
buton.pack(pady=10)

geri_buton = tk.Button(panel, text="GERİ DÖN   ⬅", font=("Georgia", 14, "bold"),
                       bg="white", fg="#000428", padx=30, pady=10, borderwidth=2,
                       command=geri_don)
geri_buton.pack(pady=10)

# Çalıştır
panel.mainloop()

