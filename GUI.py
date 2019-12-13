from tkinter import *
from PIL import ImageTk, Image
import Insert as Ins
import Scrape as Scr
from Place import Place


def start():
    window.mainloop()


def on_closing():
    try:
        Scr.end(scraper)
    except Exception:
        pass
    try:
        Ins.end(inserter)
    except Exception:
        pass
    window.destroy()


def change_logo():
    logo_img = Image.open("logo.jpg")
    logo_img = logo_img.resize((150, 150), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(logo_img)
    logo.configure(image=logo_img)
    logo.image = logo_img


def change_bg():
    bg_img = Image.open("bg.png")
    bg_img = bg_img.resize((500, 190), Image.ANTIALIAS)
    bg_img = ImageTk.PhotoImage(bg_img)
    bg.configure(image=bg_img)
    bg.image = bg_img


def scrape():
    page = fb_input.get()
    if "https://www.facebook.com/" in page:
        place = Scr.scrape(page, scraper)
        change_logo()
        change_bg()
        nazwa_input.delete(0, END)
        nazwa_input.insert(INSERT, place.nazwa)
        opis_input.delete(1.0, END)
        opis_input.insert(INSERT, place.opis)
        miasto_input.delete(0, END)
        miasto_input.insert(INSERT, place.miasto)
        adres_input.delete(0, END)
        adres_input.insert(INSERT, place.adres)
        ig_input.delete(0, END)
        ig_input.insert(INSERT, place.ig)
        email_input.delete(0, END)
        email_input.insert(INSERT, place.email)
        tel_input.delete(0, END)
        tel_input.insert(INSERT, place.tel)
        web_input.delete(0, END)
        web_input.insert(INSERT, place.web)
    else:
        fb_input.delete(0, END)
        fb_input.insert(INSERT, "Nieprawidłowy adres.")


def save():
    nazwa = nazwa_input.get()
    opis = opis_input.get(1.0, END)
    miasto = miasto_input.get()
    adres = adres_input.get()
    fb = fb_input.get()
    ig = ig_input.get()
    email = email_input.get()
    tel = tel_input.get()
    web = web_input.get()

    if fb and nazwa and miasto and adres:
        place = Place(nazwa, opis, miasto, adres, fb, ig, email, tel, web)
        Ins.insert(place, inserter)
    else:
        fb_input.delete(0, END)
        fb_input.insert(INSERT, "Brak inforamcji.")


window = Tk()
window.title("Facebook/Samplee Scraper")
window.resizable(0, 0)
window.protocol("WM_DELETE_WINDOW", on_closing)
scraper = Scr.open_driver()
inserter = Ins.login()

top = Frame(window)
top.grid(row=0, column=0)

Label(top, text="Facebook: ").grid(row=0, column=0, padx=5, pady=15)

fb_input = Entry(top, width=40)
fb_input.grid(row=0, column=1, padx=5, pady=15)

Button(top, text="Pobierz", width=7, command=scrape).grid(row=0, column=2, padx=5, pady=15)

images = Frame(window)
images.grid(row=1, column=1)

temp_logo_img = Image.open("placeholder_logo.jpg")
temp_logo_img = temp_logo_img.resize((150, 150), Image.ANTIALIAS)
temp_logo_img = ImageTk.PhotoImage(temp_logo_img)
temp_bg_img = Image.open("placeholder_bg.png")
temp_bg_img = temp_bg_img.resize((500, 190), Image.ANTIALIAS)
temp_bg_img = ImageTk.PhotoImage(temp_bg_img)
logo_container = Frame(images)
logo_container.grid(row=0)
logo = Label(logo_container, image=temp_logo_img)
logo.grid(row=0, pady=10)
Button(logo_container, text="Zmień", width=7, command=change_logo).grid(row=1)
bg_container = Frame(images)
bg_container.grid(row=1)
bg = Label(bg_container, image=temp_bg_img)
bg.grid(row=0, pady=10)
Button(bg_container, text="Zmień", width=7, command=change_bg).grid(row=1)

main = Frame(window)
main.grid(row=1, column=0)

Label(main, text="Nazwa: ").grid(row=0, column=0, padx=5, pady=5)

nazwa_input = Entry(main, width=30)
nazwa_input.grid(row=0, column=1, padx=5, pady=5)

Label(main, text="Opis: ").grid(row=1, column=0, padx=5, pady=5)

opis_input = Text(main, width=40, height=15)
opis_input.grid(row=1, column=1, padx=5, pady=5)

Label(main, text="Miasto: ").grid(row=2, column=0, padx=5, pady=5)

miasto_input = Entry(main, width=30)
miasto_input.grid(row=2, column=1, padx=5, pady=5)

Label(main, text="Adres: ").grid(row=3, column=0, padx=5, pady=5)

adres_input = Entry(main, width=30)
adres_input.grid(row=3, column=1, padx=5, pady=5)

Label(main, text="Instagram: ").grid(row=4, column=0, padx=5, pady=5)

ig_input = Entry(main, width=30)
ig_input.grid(row=4, column=1, padx=5, pady=5)

Label(main, text="Email: ").grid(row=5, column=0, padx=5, pady=5)

email_input = Entry(main, width=30)
email_input.grid(row=5, column=1, padx=5, pady=5)

Label(main, text="Telefon: ").grid(row=6, column=0, padx=5, pady=5)

tel_input = Entry(main, width=30)
tel_input.grid(row=6, column=1, padx=5, pady=5)

Label(main, text="Web: ").grid(row=7, column=0, padx=5, pady=5)

web_input = Entry(main, width=30)
web_input.grid(row=7, column=1, padx=5, pady=5)

bot = Frame(window)
bot.grid(row=2, column=0)

Button(bot, text="Zapisz", width=7, command=save).grid(row=0, column=0, padx=5, pady=15)
