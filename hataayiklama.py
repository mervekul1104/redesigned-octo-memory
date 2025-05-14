from tkinter import Tk, Label, Frame, Text, Button, END
from PIL import Image, ImageTk

def kodu_ayıkla():
    kod_kutusu.delete("1.0", END)  # Önce temizle
    ayıklanmıs_kod = """ayıklanmıs kod"""
    kod_kutusu.insert(END, ayıklanmıs_kod)

# Ana pencere
pencere = Tk()
pencere.title("Hata Ayıkla")
pencere.geometry("1280x720")
pencere.configure(bg="#000428")

# Arka plan resmi
background_image = Image.open("background.png")  # Arka plan resmi dosyan olmalı
background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(background_image)
bg_label = Label(pencere, image=bg_photo)
bg_label.image = bg_photo  # Referansı tut
bg_label.place(relwidth=1, relheight=1)

# Başlık
baslik = Label(pencere, text="Hata Ayıklama", font=("Georgia", 30, "bold"),
               fg="white", bg="#000428")
baslik.pack(pady=(30, 10))

# Alt çizgi
cizgi = Frame(pencere, bg="white", height=2, width=300)
cizgi.pack(pady=5)

# Kod kutusu
kod_kutusu = Text(pencere, bg="black", fg="lime", width=108, height=22,
                  font=("Courier New", 12))
kod_kutusu.pack(pady=40)

# Buton
buton = Button(pencere, text="Hata Ayıkla   ➤", font=("Georgia", 14, "bold"),
               bg="white", fg="#000428", padx=30, pady=10, borderwidth=2,
               command=kodu_ayıkla)
buton.pack(pady=10)

# Çalıştır
pencere.mainloop()
