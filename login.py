import subprocess
from tkinter import Tk, Label, Entry, Button, messagebox
from PIL import Image, ImageTk
from main import main_page


# Giriş bilgileri
KULLANICI_ADI = "admin"
SIFRE = "1234"

def mainbaglama():
    login.destroy()
    subprocess.run(["python", "main.py"])

def forgot_password():
    messagebox.showinfo("Şifre Sıfırlama", "Şifre sıfırlama işlemi için e-posta gönderilecek.")

# Ana arayüz (giriş sonrası çalışacak olan senin önceki arayüzün buraya taşınabilir)
def ana_ekran():
    ana = Tk()
    ana.title("Ana Ekran")
    ana.geometry("1280x720")

    # Arka plan resmi
    background_image = Image.open("background.png")  # Arka plan resmi (senin arayüzdeki)
    background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(background_image)

    bg_label = Label(ana, image=bg_photo)
    bg_label.image = bg_photo  # referans tutmazsan kaybolur
    bg_label.place(relwidth=1, relheight=1)

    # Basit bir hoş geldin yazısı (buraya senin asıl GUI kodların gelecek)
    Label(ana, text="WELCOME TO CQR", font=("JetBrains Mono", 32), fg="white", bg="black").place(relx=0.5, rely=0.1, anchor="center")

    ana.mainloop()

# Giriş kontrolü
def giris_kontrol():
    kullanici = kullanici_entry.get()
    sifre = sifre_entry.get()
    if kullanici == KULLANICI_ADI and sifre == SIFRE:
        messagebox.showinfo("Giriş Başarılı", "Hoş geldiniz!")
        mainbaglama()

    else:
        messagebox.showerror("Hatalı Giriş", "Kullanıcı adı veya şifre yanlış.")

# Login ekranı
login = Tk()
login.title("Giriş Ekranı")
login.geometry("1280x720")

# Arka plan resmi yükle
bg_image = Image.open("background.png")  # Login arka planı
bg_image = bg_image.resize((1280, 720), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(login, image=bg_photo)
bg_label.image = bg_photo  # Referans kaybolmasın diye
bg_label.place(relwidth=1, relheight=1)

text_label = Label(login, text="WELCOME TO CQR", font=("JetBrains Mono", 32), fg="white", bg="black")
text_label.place(relx=0.5, rely=0.1, anchor="center")

# Giriş kutuları
Label(login, text="Kullanıcı Adı",bg="#080c2c", fg="white", font=("Arial", 12, "bold")).place(x=527, y=272)
kullanici_entry = Entry(login,font=("Arial", 17))
kullanici_entry.place(x=530, y=295)

Label(login, text="Şifre", bg="#080c2c", fg="white",font=("Arial", 12, "bold")).place(x=524, y=327)
sifre_entry = Entry(login, show="*", font=("Arial",17))
sifre_entry.place(x=530, y=350)

Button(login, text="Giriş Yap", command=giris_kontrol,font=("Arial", 14, "bold"),width=21,height=1).place(x=530, y=400,relwidth=0.207)
Button(login, text="Şifremi Unuttum",bg="#046cac",fg="blue", cursor="hand2", bd=0, command=forgot_password).place(x=703, y=440,relwidth=0.07,relheight=0.025)

login.mainloop()
