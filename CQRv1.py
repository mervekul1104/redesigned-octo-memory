import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import Label, Frame, Text, Button,Canvas
from PIL import Image, ImageTk
from google import genai
import json
import os
import customtkinter as ctk
from customtkinter import CTkFont

client = genai.Client(api_key="AIzaSyCuplLWWIlDFkglTzhJUpUt2iPkbM-3YUI")
ctk.set_appearance_mode("light")  # light / dark
ctk.set_default_color_theme("blue")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CQR")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.username = "Misafir"

        # Arka plan resmi
        background_image = Image.open("background.png")  # PIL Image
        background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)  # PIL Image
        bg_photo = ImageTk.PhotoImage(background_image)  # Tkinter PhotoImage

        bg_label = Label(self, image=bg_photo)
        bg_label.image = bg_photo  # referansı tut (garbage collection engelle)
        bg_label.place(relwidth=1, relheight=1)

        # Sayfalar (Frames)
        self.frames = {}
        for F in (RegisterPage,LoginPage, MainPage, IyilestirmePage, HataAyiklamaPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("LoginPage")

    def fade_out(self, step=0.7, callback=None):
        alpha = self.attributes("-alpha")
        if alpha > 0:
            alpha -= step
            if alpha < 0:
                alpha = 0
            self.attributes("-alpha", alpha)
            self.after(25, self.fade_out, step, callback)
        else:
            if callback:
                callback()

    def fade_in(self, step=0.7):
        alpha = self.attributes("-alpha")
        if alpha < 1:
            alpha += step
            if alpha > 1:
                alpha = 1
            self.attributes("-alpha", alpha)
            self.after(25, self.fade_in, step)

    def show_frame(self, page_name):
        def change_frame():
            frame = self.frames[page_name]
            frame.tkraise()
            self.fade_in()

        self.fade_out(callback=change_frame)

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.kullanicilar = self.kullanicilari_yukle()

        background_image = Image.open("yeniloginbeyaz.png")  # PIL Image
        background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)  # PIL Image
        bg_photo = ImageTk.PhotoImage(background_image)  # Tkinter PhotoImage

        bg_label = Label(self, image=bg_photo)
        bg_label.image = bg_photo  # referansı tut (garbage collection engelle)
        bg_label.place(relwidth=1, relheight=1)

        text_label = Label(self, text="CQR", font=("Orbitron", 30), fg="#1799A9", bg="#000724")
        text_label.place(relx=0.08, rely=0.1, anchor="center")

        canvasL = Canvas(self, width=220, height=5, bg="#000724", bd=0, highlightthickness=0)
        canvasL.place(relx=0.12, rely=0.15, anchor="center")
        canvasL.create_line(0, 5, 280, 5, fill="#1799A9", width=2)

        # Başlık
        label_user = ctk.CTkLabel(self, text="Kullanıcı Adı:", font=ctk.CTkFont(size=18), text_color="black",
                                  bg_color="white")
        label_user.place(x=563, y=240)

        self.username_entry = ctk.CTkEntry(self, font=ctk.CTkFont(size=14),
                                           placeholder_text="Kullanıcı Adınızı Girin")
        self.username_entry.place(x=563, y=280)

        label_pass = ctk.CTkLabel(self, text="Şifre:", font=ctk.CTkFont(size=18), text_color="black", bg_color="white")
        label_pass.place(x=563, y=320)

        self.password_entry = ctk.CTkEntry(self, font=ctk.CTkFont(size=14), show="*",
                                           placeholder_text="Şifrenizi Girin")
        self.password_entry.place(x=563, y=360)

        # Giriş Butonu
        login_button = ctk.CTkButton(self, text="Giriş Yap", font=ctk.CTkFont(size=16),
                                     fg_color="#fdc886", hover_color="#f5a742", text_color="black",
                                     command=self.login)
        login_button.place(x=563, y=415, )

        # Kayıt Ol Butonu
        register_button = ctk.CTkButton(self, text="Hesabınız yok mu? Kayıt ol", font=ctk.CTkFont(size=10),
                                        fg_color="white", hover_color="#FAF1F1", text_color="Black",
                                        command=lambda: controller.show_frame("RegisterPage"))
        register_button.place(x=563, y=460, )

    def kullanicilari_yukle(self):
        # JSON dosyası varsa yükle, yoksa boş sözlük döndür
        if os.path.exists("kullanicilar.json"):
            with open("kullanicilar.json", "r") as f:
                return json.load(f)
        else:
            return {}

    def kullanicilari_kaydet(self):
        # Güncel kullanıcı listesini dosyaya yaz
        with open("kullanicilar.json", "w") as f:
            json.dump(self.kullanicilar, f, indent=4)
    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş olamaz!")
            return

        if username not in self.kullanicilar:
            messagebox.showerror("Hata", "Kullanıcı adı veya Şifre yanlış!")
            return

        if self.kullanicilar[username] != password:
            messagebox.showerror("Hata", "Kullanıcı adı veya Şifre yanlış!")
            return

        # Başarılı giriş
        self.controller.set_username(username)
        self.controller.show_frame("MainPage")

class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        background_image = Image.open("yeniloginbeyaz.png")  # PIL Image
        background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)  # PIL Image
        bg_photo = ImageTk.PhotoImage(background_image)  # Tkinter PhotoImage

        bg_label = Label(self, image=bg_photo)
        bg_label.image = bg_photo  # referansı tut (garbage collection engelle)
        bg_label.place(relwidth=1, relheight=1)


        text_label = Label(self, text="CQR", font=("Orbitron", 30), fg="#1799A9", bg="#000724")
        text_label.place(relx=0.08, rely=0.1, anchor="center")

        canvasL = Canvas(self, width=220, height=5, bg="#000724", bd=0, highlightthickness=0)
        canvasL.place(relx=0.12, rely=0.15, anchor="center")
        canvasL.create_line(0, 5, 280, 5, fill="#1799A9", width=2)

        # Başlık
        label_user = ctk.CTkLabel(self, text="Yeni Kullanıcı Adı:", font=ctk.CTkFont(size=18), text_color="black",bg_color="white")
        label_user.place(x=563, y=240)

        self.new_username = ctk.CTkEntry(self, font=ctk.CTkFont(size=14),
                                           placeholder_text="Kullanıcı Adınızı Girin")
        self.new_username.place(x=563, y=280)

        label_pass = ctk.CTkLabel(self, text="Yeni Şifre:", font=ctk.CTkFont(size=18), text_color="black",bg_color="white")
        label_pass.place(x=563, y=320)

        self.new_password = ctk.CTkEntry(self, font=ctk.CTkFont(size=14), show="*",
                                           placeholder_text="Şifrenizi Girin")
        self.new_password.place(x=563, y=360)

        register_button = ctk.CTkButton(self, text="Kaydı Tamamla", font=ctk.CTkFont(size=16),
                                     fg_color="#66FF66", hover_color="green", text_color="black",
                                     command=self.register_user)
        register_button.place(x=563, y=415)

        geri_button = ctk.CTkButton(self, text="Geri Dön", font=ctk.CTkFont(size=16),
                                     fg_color="#fdc886", hover_color="#f5a742", text_color="black",
                                     command=lambda: controller.show_frame("LoginPage"))
        geri_button.place(x=563, y=460)

    def register_user(self):
        username = self.new_username.get().strip()
        password = self.new_password.get().strip()

        if not username or not password:
            messagebox.showerror("Hata", "Kullanıcı adı ve şifre boş bırakılamaz.")
            return

        # LoginPage içindeki kullanıcı listesine eriş
        login_page = self.controller.frames["LoginPage"]

        if username in login_page.kullanicilar:
            messagebox.showerror("Hata", "Bu kullanıcı adı zaten mevcut.")
            return

        # Yeni kullanıcıyı sözlüğe ekle
        login_page.kullanicilar[username] = password

        # Dosyaya kaydet
        login_page.kullanicilari_kaydet()

        messagebox.showinfo("Başarılı", "Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
        self.controller.show_frame("LoginPage")

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        background_image = Image.open("arkaplan.jpg")  # PIL Image
        background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)  # PIL Image
        bg_photo = ImageTk.PhotoImage(background_image)  # Tkinter PhotoImage

        bg_label = Label(self, image=bg_photo)
        bg_label.image = bg_photo  # referansı tut (garbage collection engelle)
        bg_label.place(relwidth=1, relheight=1)

        self.welcome_label = Label(self, font=("Arial", 18), fg="white", bg="#000626")
        self.welcome_label.place(relx=0.99, rely=0.02, anchor="ne")

        title_label = Label(self, text="WELCOME TO CQR", font=("JetBrains Mono", 32), fg="white", bg="#000623")
        title_label.place(relx=0.5, rely=0.1, anchor="center")

        def iyilestir_buton():
            controller.show_frame("IyilestirmePage")

        iyilestir_button = Button(self, text="İyileştir", anchor="n", font=("Arial", 23), bg="Green", fg="white",
                                  command=iyilestir_buton)
        iyilestir_button.place(relx=0.3, rely=0.5, anchor="center", width=250, height=150)

        canvas1 = Canvas(self, width=250, height=10, bg="green", bd=0, highlightthickness=0)
        canvas1.place(relx=0.3, rely=0.47, anchor="center")
        canvas1.create_line(0, 5, 280, 5, fill="black", width=2)

        iyilestir_aciklama = Label(self, text="Kodunuzu iyileştirerek geliştirilmiş bir versiyon oluşturun.",
                                   font=("Arial", 10), fg="white", bg="green", wraplength=200)
        iyilestir_aciklama.place(relx=0.3, rely=0.51, anchor="center")

        iyilestir_aciklama.bind("<Button-1>", lambda e: iyilestir_buton())
        canvas1.bind("<Button-1>", lambda e: iyilestir_buton())

        def hata_ayikla_buton():
            controller.show_frame("HataAyiklamaPage")

        hata_ayikla_button = Button(self, text="Hata Ayıkla", anchor="n", font=("Arial", 20), bg="navy", fg="white",
                                    command=hata_ayikla_buton)
        hata_ayikla_button.place(relx=0.7, rely=0.5, anchor="center", width=250, height=150)

        canvas2 = Canvas(self, width=250, height=10, bg="navy", bd=0, highlightthickness=0)
        canvas2.place(relx=0.7, rely=0.47, anchor="center")
        canvas2.create_line(0, 5, 280, 5, fill="black", width=2)

        hataayikla_aciklama = Label(self,
                                    text="Kodunuzu analiz ederek mevcut hataları tespit etmek ve açıklamalarıyla birlikte listelemek için tıklayınız.",
                                    font=("Arial", 10), fg="white", bg="navy", wraplength=200)
        hataayikla_aciklama.place(relx=0.7, rely=0.53, anchor="center")

        hataayikla_aciklama.bind("<Button-1>", lambda e: hata_ayikla_buton())
        canvas2.bind("<Button-1>", lambda e: hata_ayikla_buton())


        logout_button = Button(self, text="Çıkış Yap", font=("Arial", 13), bg="red", fg="white",
                               command=self.logout)
        logout_button.place(relx=0.95, rely=0.1, anchor="center", width=95, height=30)

    def tkraise(self, *args, **kwargs):
        username = self.controller.get_username()
        self.welcome_label.config(text=f"Hoş geldin, {username}!")
        super().tkraise(*args, **kwargs)

    def logout(self):
        self.controller.set_username("Misafir")
        self.controller.show_frame("LoginPage")


class IyilestirmePage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        background_image = Image.open("arkaplan.jpg")  # PIL Image
        background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)  # PIL Image
        bg_photo = ImageTk.PhotoImage(background_image)  # Tkinter PhotoImage

        bg_label = Label(self, image=bg_photo)
        bg_label.image = bg_photo  # referansı tut (garbage collection engelle)
        bg_label.place(relwidth=1, relheight=1)

        baslik = Label(self, text="İYİLEŞTİRME", font=("Georgia", 30, "bold"), fg="white", bg="#070c2f")
        baslik.pack(pady=(30, 10))

        cizgi = Frame(self, bg="black", height=2, width=300)
        cizgi.pack(pady=5)

        kod_frame = Frame(self, bg="#000428")
        kod_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        scrollbar_y = tk.Scrollbar(kod_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_x = tk.Scrollbar(kod_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.kod_kutusu = Text(kod_frame, bg="black", fg="lime", font=("Courier New", 12),
                               yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, wrap="none")
        self.kod_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_y.config(command=self.kod_kutusu.yview)
        scrollbar_x.config(command=self.kod_kutusu.xview)

        iyilestir_btn = Button(self, text="İYİLEŞTİR   ➤", font=("Georgia", 14, "bold"),
                               bg="green", fg="white", padx=30, pady=10, borderwidth=2,
                               command=self.kodu_iyilestir)
        iyilestir_btn.pack(pady=10)

        geri_btn = Button(self, text="GERİ DÖN   ⬅", font=("Georgia", 14, "bold"),
                          bg="red", fg="white", padx=30, pady=10, borderwidth=2,
                          command=lambda: controller.show_frame("MainPage"))
        geri_btn.pack(pady=10)

    def kod_iyilestir(self, kod):
        # Burada api çağrısı yapabilirsin, şu an yorum satırı:
        prompt = f"Kurallar: 1.Sen bir yazılım geliştirme uzmanısın. Aşağıdaki kodu daha iyi, optimize ve okunabilir hale getir ama açıklama yapmadan sadece iyileştirilmiş kodu çıktı olarak ver. 2. Eğer kodda 'Lütfen önce bir kod yazınız' yazıyorsa herhangi bir cevap verme yalnızca kod olanlara bir cevap ver.:\n\n{kod}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text

    def kodu_iyilestir(self):
        kod = self.kod_kutusu.get("1.0", tk.END).strip()
        if not kod:
            self.kod_kutusu.delete("1.0", tk.END)
            self.kod_kutusu.insert(tk.END, "Lütfen önce kod kutusuna kod yazınız.")
            return

        try:
            iyilestirilmis_kod = self.kod_iyilestir(kod)
        except Exception as e:
            iyilestirilmis_kod = f"Hata oluştu: {e}"

        self.kod_kutusu.delete("1.0", tk.END)
        self.kod_kutusu.insert(tk.END, iyilestirilmis_kod)


class HataAyiklamaPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        background_image = Image.open("arkaplan.jpg")  # PIL Image
        background_image = background_image.resize((1280, 720), Image.Resampling.LANCZOS)  # PIL Image
        bg_photo = ImageTk.PhotoImage(background_image)  # Tkinter PhotoImage

        bg_label = Label(self, image=bg_photo)
        bg_label.image = bg_photo  # referansı tut (garbage collection engelle)
        bg_label.place(relwidth=1, relheight=1)

        baslik = Label(self, text="Hata Ayıklama", font=("Georgia", 30, "bold"), fg="white", bg="#070c2f")
        baslik.pack(pady=(30, 10))

        cizgi = Frame(self, bg="black", height=2, width=300)
        cizgi.pack(pady=5)

        kod_frame = Frame(self, bg="#000428")
        kod_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        scrollbar_y = tk.Scrollbar(kod_frame)
        scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        scrollbar_x = tk.Scrollbar(kod_frame, orient=tk.HORIZONTAL)
        scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.kod_kutusu = Text(kod_frame, bg="black", fg="lime", font=("Courier New", 12),
                               yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, wrap="none")
        self.kod_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar_y.config(command=self.kod_kutusu.yview)
        scrollbar_x.config(command=self.kod_kutusu.xview)

        ayikla_btn = Button(self, text="Hata Ayıkla   ➤", font=("Georgia", 14, "bold"),
                            bg="blue", fg="white", padx=30, pady=10, borderwidth=2,
                            command=self.kodu_ayikla)
        ayikla_btn.pack(pady=10)

        geri_btn = Button(self, text="GERİ DÖN   ⬅", font=("Georgia", 14, "bold"),
                          bg="red", fg="white", padx=30, pady=10, borderwidth=2,
                          command=lambda: controller.show_frame("MainPage"))
        geri_btn.pack(pady=10)

    def kodu_ayikla(self):
        kod = self.kod_kutusu.get("1.0", tk.END).strip()
        if not kod:
            self.kod_kutusu.delete("1.0", tk.END)
            self.kod_kutusu.insert(tk.END, "Lütfen önce kod kutusuna kod yazınız.")
            return

        try:
            duzeltilmis_kod = self.kod_hata_ayikla(kod)
        except Exception as e:
            duzeltilmis_kod = f"Hata oluştu: {e}"

        self.kod_kutusu.delete("1.0", tk.END)
        self.kod_kutusu.insert(tk.END, duzeltilmis_kod)

    def kod_hata_ayikla(self, kod):
        # API çağrısı burada yapılabilir, şimdilik sadece inputu dönüyor
        prompt = f"Kurallar: 1.Sen bir yazılım geliştirme uzmanısın. Aşağıdaki koddaki hataları (varsa) düzelt ama açıklama yapmadan sadece düzeltilmiş kodu çıktı olarak ver. 2. Eğer kodda 'Lütfen önce bir kod yazınız' yazıyorsa herhangi bir cevap verme yalnızca kod olanlara bir cevap ver.:\n\n{kod}"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text




if __name__ == "__main__":
    app = App()
    app.mainloop()

