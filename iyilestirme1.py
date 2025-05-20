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

def kod_iyilestir(kod):
    prompt = f"Sen bir yazılım geliştirme uzmanısın. Aşağıdaki kodu daha iyi, optimize ve okunabilir hale getir ama açıklama yapmadan sadece iyileştirilmiş kodu çıktı olarak ver:\n\n{kod}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

def kodu_iyilestir():
    kod = kod_kutusu.get("1.0", tk.END).strip()
    if not kod:
        kod_kutusu.delete("1.0", tk.END)
        kod_kutusu.insert(tk.END, "Lütfen önce kod kutusuna kod yazınız.")
        return

    try:
        iyilestirilmis_kod = kod_iyilestir(kod)
    except Exception as e:
        iyilestirilmis_kod = f"Hata oluştu: {e}"

    kod_kutusu.delete("1.0", tk.END)
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

kod_frame = tk.Frame(panel, bg="#000428")
kod_frame.pack(pady=40, fill=tk.BOTH, expand=True)

scrollbar_y = tk.Scrollbar(kod_frame)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_x = tk.Scrollbar(kod_frame, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

kod_kutusu = Text(kod_frame, bg="black", fg="lime", width=108, height=22,
                  font=("Courier New", 12),
                  yscrollcommand=scrollbar_y.set,
                  xscrollcommand=scrollbar_x.set,
                  wrap="none")
kod_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_y.config(command=kod_kutusu.yview)
scrollbar_x.config(command=kod_kutusu.xview)


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

