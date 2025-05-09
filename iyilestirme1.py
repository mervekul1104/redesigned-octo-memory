import tkinter as tk
from tkinter import Label, Frame, Text

def kodu_iyilestir():
    kod_kutusu.delete("1.0", tk.END)  # Önce temizle
    iyilestirilmis_kod = """def toplama(a, b):
    return a + b"""
    kod_kutusu.insert(tk.END, iyilestirilmis_kod)

# Ana pencere
pencere = tk.Tk()
pencere.title("İyileştirme")
pencere.geometry("1000x600")
pencere.configure(bg="#000428")

# Başlık
baslik = Label(pencere, text="İYİLEŞTİRME", font=("Georgia", 30, "bold"),
               fg="white", bg="#000428")
baslik.pack(pady=(30, 10))

# Alt çizgi
cizgi = Frame(pencere, bg="white", height=2, width=300)
cizgi.pack(pady=5)

# Kod kutusu (text alanı gibi davranan siyah kutu)
kod_kutusu = Text(pencere, bg="black", fg="lime", width=108, height=15,
                  font=("Courier New", 12))
kod_kutusu.pack(pady=40)

# Buton
buton = tk.Button(pencere, text="İYİLEŞTİR   ➤", font=("Georgia", 14, "bold"),
                  bg="white", fg="#000428", padx=30, pady=10, borderwidth=2,
                  command=kodu_iyilestir)
buton.pack(pady=10)

# Çalıştır
pencere.mainloop()