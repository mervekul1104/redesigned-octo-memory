import subprocess
import tkinter as tk
from tkinter import Label, Frame, Text
from PIL import Image, ImageTk
import sys

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Misafir"

def kodu_ayıkla():
    kod_kutusu.delete("1.0", tk.END)  # Önce temizle
    ayıklanmıs_kod = """ayıklanmıs kod"""
    kod_kutusu.insert(tk.END, ayıklanmıs_kod)

def geri_don():
    debug_console.destroy()  # Bu pencereyi kapat
    subprocess.run(["python", "main.py",username])

# Ana pencere
debug_console = tk.Tk()
debug_console.title("Hata Ayıkla")
debug_console.geometry("1280x720")
debug_console.configure(bg="#000428")

# Arka plan resmi
background_image = Image.open("background.png")  # Arka plan resmi dosyan olmalı
background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(background_image)
bg_label = Label(debug_console, image=bg_photo)
bg_label.image = bg_photo  # Referansı tut
bg_label.place(relwidth=1, relheight=1)

# Başlık
baslik = Label(debug_console, text="Hata Ayıklama", font=("Georgia", 30, "bold"),
               fg="white", bg="#000428")
baslik.pack(pady=(30, 10))

# Alt çizgi
cizgi = Frame(debug_console, bg="white", height=2, width=300)
cizgi.pack(pady=5)

# Kod kutusu
kod_kutusu = Text(debug_console, bg="black", fg="lime", width=108, height=22,
                  font=("Courier New", 12))
kod_kutusu.pack(pady=40)

# Buton
buton = tk.Button(debug_console, text="Hata Ayıkla   ➤", font=("Georgia", 14, "bold"),
               bg="white", fg="#000428", padx=30, pady=10, borderwidth=2,
               command=kodu_ayıkla)
buton.pack(pady=10)

geri_buton = tk.Button(debug_console, text="GERİ DÖN   ⬅", font=("Georgia", 14, "bold"),
                       bg="white", fg="#000428", padx=30, pady=10, borderwidth=2,
                       command=geri_don)
geri_buton.pack(pady=10)

# Çalıştır
debug_console.mainloop()

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Misafir"