import subprocess
import sys
from tkinter import Tk, Label, Frame, Canvas,Button
from PIL import Image, ImageTk
import time


def main_page(username):
    # Ana pencereyi oluştur
    main = Tk()
    main.title("Arka Planlı Arayüz")
    main.geometry("1280x720")  # Pencere boyutları (genişlik x yükseklik)

    # Arka plan resmini yükle
    background_image = Image.open("background.png")  # Resmin yolu
    background_image = background_image.resize((1280, 720),
                                               Image.Resampling.LANCZOS)  # Pencere boyutuna göre yeniden boyutlandır
    bg_photo = ImageTk.PhotoImage(background_image)

    # Arka plan etiketi oluştur ve resmi buraya ekle
    bg_label = Label(main, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)  # Resmi tüm pencereyi kaplayacak şekilde yerleştir

    welcome_label = Label(main, text=f"Hoş geldin, {username}!", font=("Arial", 18), fg="white", bg="black")
    welcome_label.place(relx=0.99, rely=0.02, anchor="ne")

    def logout():
        main.destroy()
        subprocess.run(["python", "login.py"])

    logout_button = Button(main, text="Çıkış Yap", command=logout, font=("Arial", 12), bg="red", fg="white")
    logout_button.place(relx=0.99, rely=0.08, anchor="ne")

    text_label = Label(main, text="WELCOME TO CQR", font=("JetBrains Mono", 32), fg="white", bg="black")
    text_label.place(relx=0.5, rely=0.1, anchor="center")  # Pencerenin ortasına yerleştir

    selection_frame_1 = Frame(main, width=300, height=300, bg="navy", bd=10, relief="raised")
    selection_frame_1.place(relx=0.25, rely=0.7, anchor="center")  # İlk kutu

    selection_frame_2 = Frame(main, width=300, height=300, bg="navy", bd=10, relief="raised")
    selection_frame_2.place(relx=0.75, rely=0.7, anchor="center")  # İkinci kutu

    # "İyileştir" yazısını ve açıklamasını ekleyelim (sol kutu)
    improve_label = Label(selection_frame_1, text="İyileştir", font=("Arial", 24, "bold"), fg="white", bg="navy")
    improve_label.place(relx=0.5, rely=0.2, anchor="center")  # Başlık

    canvas1 = Canvas(selection_frame_1, width=280, height=10, bg="navy", bd=0, highlightthickness=0)
    canvas1.place(relx=0.5, rely=0.4, anchor="center")  # Çizgiyi başlık ve açıklama arasına yerleştiriyoruz
    canvas1.create_line(0, 5, 280, 5, fill="white", width=2)

    # "İyileştir" alt açıklamasını ekleyelim
    improve_description = Label(selection_frame_1, text="Kodunuzu iyileştirerek geliştirilmiş bir versiyon oluşturun.",
                                font=("Arial", 12), fg="white", bg="navy",
                                wraplength=280)  # wraplength burada doğru şekilde kullanıldı
    improve_description.place(relx=0.5, rely=0.65, anchor="center")  # Alt açıklama  # Alt açıklama

    # Sağdaki kutuya "Hata ayıkla" yazısını ve açıklamasını ekleyelim
    debug_label = Label(selection_frame_2, text="Hata ayıkla", font=("Arial", 24, "bold"), fg="white", bg="navy")
    debug_label.place(relx=0.5, rely=0.2, anchor="center")  # Başlık

    canvas2 = Canvas(selection_frame_2, width=280, height=10, bg="navy", bd=0, highlightthickness=0)
    canvas2.place(relx=0.5, rely=0.4, anchor="center")  # Çizgiyi başlık ve açıklama arasına yerleştiriyoruz
    canvas2.create_line(0, 5, 280, 5, fill="white", width=2)

    # "Hata ayıkla" alt açıklamasını ekleyelim
    debug_description = Label(selection_frame_2,
                              text="Kodunuzu analiz ederek mevcut hataları tespit etmek ve açıklamalarıyla birlikte listelemek için tıklayınız.",
                              font=("Arial", 12), fg="white", bg="navy",
                              wraplength=280)  # wraplength burada doğru şekilde kullanıldı
    debug_description.place(relx=0.5, rely=0.65, anchor="center")  # Alt açıklama

    # Kare kutulara tıklama olayı ekleyelim
    def change_bd(frame):
        frame.config(bd=3)  # Çerçeveyi değiştir
        main.after(600, lambda: frame.config(bd=10))  # 1 saniye sonra geri eski haline getir

    def reset_bd(frame):
        frame.config(bd="10")  # Rengi eski haline getir

    # Kare kutulara tıklama olayı ekleyelim
    def on_click(frame_num):
        if frame_num == 1:
            change_bd(selection_frame_1)
            main.destroy()
            subprocess.run(["python", "iyilestirme1.py", username]) # İyileştirme sayfasını aç
        elif frame_num == 2:
            change_bd(selection_frame_2)
            main.destroy()
            subprocess.run(["python", "hataayiklama.py", username])

    # Kare kutulara tıklama olayları ekleyelim
    selection_frame_1.bind("<Button-1>", lambda e: on_click(1))
    selection_frame_2.bind("<Button-1>", lambda e: on_click(2))

    # Ana döngüyü başlat
    main.mainloop()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = "Misafir"
    main_page(username)