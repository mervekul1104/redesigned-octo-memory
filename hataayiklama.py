import subprocess
import tkinter as tk
from tkinter import Label, Frame, Text
from PIL import Image, ImageTk
import sys
from google import genai

client = genai.Client(api_key="AIzaSyCuplLWWIlDFkglTzhJUpUt2iPkbM-3YUI")

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    username = "Misafir"

def kod_hata_ayikla(kod):
    prompt = f"Bu kodda hata var mı kontrol et ve varsa hataları belirt, ayrıca hataları düzelt:\n\n{kod}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

def kodu_ayıkla():
    kod = kod_kutusu.get("1.0", tk.END).strip()
    if not kod:
        kod_kutusu.delete("1.0", tk.END)
        kod_kutusu.insert(tk.END, "Lütfen önce kod kutusuna kod yazınız.")
        return
    try:
        ayıklanmıs_kod = kod_hata_ayikla(kod)
    except Exception as e:
        ayıklanmıs_kod = f"Hata oluştu: {e}"

    kod_kutusu.delete("1.0", tk.END)
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
kod_frame = tk.Frame(debug_console, bg="#000428")
kod_frame.pack(pady=40, fill=tk.BOTH, expand=True)

scrollbar_y = tk.Scrollbar(kod_frame)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_x = tk.Scrollbar(kod_frame, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

# Kod kutusu aynı frame içine alındı
kod_kutusu = Text(kod_frame, bg="black", fg="lime", width=108, height=22,
                  font=("Courier New", 12),
                  yscrollcommand=scrollbar_y.set,
                  xscrollcommand=scrollbar_x.set,
                  wrap="none")
kod_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_y.config(command=kod_kutusu.yview)
scrollbar_x.config(command=kod_kutusu.xview)

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