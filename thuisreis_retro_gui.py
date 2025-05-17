import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkinter import ttk
import random
import os
import calendar
import math
from utils import get_affirmations, emotionele_thema_suggesties
import pylunar 



BESTAND = "thuireis_journal.txt"

affirmaties = get_affirmations("affirmations.txt")

moods = [
    "😊 Blij",
    "😔 Verdrietig",
    "😐 Neutraal",
    "😖 Gestresst",
    "😌 Kalm",
    "🥺 Kwetsbaar",
    "🤍 Vol liefde",
]

behoefte_opties = ["rust", "energie", "richting", "liefde", "steun", "warmte"]

# Functie om suggesties te genereren op basis van gevoelens
def genereer_suggesties(tekst):
    gevonden = []
    tekst_lc = tekst.lower()
    for thema in emotionele_thema_suggesties.values():
        if any(woord in tekst_lc for woord in thema["woorden"]):
            gevonden.append(f"- {thema['suggestie']}")
    return "\n".join(gevonden) if gevonden else "Geen specifieke suggesties gevonden."

# NOTE: helpfunctie om venster te centreren MacOS
def center_window(window, width=680, height=830):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")
    justify="center"

# NOTE: hoofdvenster en stijl
root = tk.Tk()
root.title("Thuisreis – Naomi's Journey Home")
center_window(root)
root.configure(bg="#f5f0e1")

# NOTE: Stijl
style = ttk.Style()
style.theme_use("clam")

# NOTE: stijl lookup
frame_bg = style.lookup("TFrame", "background")
label_bg = style.lookup("TLabel", "background")
labelframe_bg = style.lookup("TLabelframe", "background")

style.configure("TButton", font=("Helvetica Neue", 12), padding=6)
style.configure("Custom.TFrame", font=(" Helvetica Neue", 12))
style.configure("Custom.TLabel", expand=True)
style.configure("Custom.TLabelframe", expand=True)
style.configure("Custom.TLabelframe.Label", expand=True)

# NOTE: maak container voor paginawisseling
container = ttk.Frame(root, padding=30, style="Custom.TFrame")
container.pack(fill="both", expand=True)

# NOTE: opslaan alle frames in dict
pages = {}

for page_name in ["Start", "Notitie", "Geschiedenis", "Kalender", "MaanstandVandaag", "Suggesties"]:
    frame = ttk.Frame(container)
    frame.grid(row=0, column=0, pady=20, sticky="nsew")
    pages[page_name] = frame

# FUNCTION: pagina wisselen
def show_page(page_name):
    pages[page_name].tkraise()

# PAGE: startmenu
home = pages["Start"]
ttk.Label(home, text="Welkom bij Naomi's Thuisreis", style="Custom.TLabel", justify="center", 
    font=("Helvetica Neue", 16, "bold")).pack(pady=5)

# Introtekst
ttk.Label(
    home,
    text=(
        "Welkom in jouw persoonlijke dagboekruimte. ❤️\n\n"
        "Deze app draait alleen lokaal, dus niemand kan hierbij. Hier kun je veilig schrijven over hoe je je voelt in de eerste maanden waarin je je nieuwe plek ontdekt. Ik hoop dat je zo altijd rust kunt vinden in een dagelijkse affirmatie, en steun kunt ontvangen via goedbedoelde suggesties en tips (of eventueel de maanstand). Neem je tijd, adem diep, en laat dit een plek zijn waar je steeds opnieuw mag thuiskomen."
    ),
    style="Custom.TLabel",
    font=("Helvetica Neue", 11, "italic"),
    anchor="center",
    justify="center",
    wraplength=600,
).pack(pady=(30, 30))

# Groepeer knoppen in een frame
button_frame = ttk.Frame(home, style="Custom.TFrame")
button_frame.pack()

# Standaard knopstijl
knop_breedte = 30
knop_stijl = {"width": knop_breedte}

ttk.Button(button_frame, text="Schrijf een dagboeknotitie", **knop_stijl, command=lambda: show_page("Notitie")).pack(pady=5)
ttk.Button(button_frame, text="Bekijk geschiedenis", **knop_stijl, command=lambda: [laad_dagboek(), show_page("Geschiedenis")]).pack(pady=5)
ttk.Button(button_frame, text="Kalender bekijken", **knop_stijl, command=lambda: [update_kalender(), show_page("Kalender")]).pack(pady=5)
ttk.Button(
    button_frame,
    text="Stand van de Maan",
    **knop_stijl,
    command=lambda: show_page("MaanstandVandaag")
).pack(pady=5)
ttk.Button(
    button_frame,
    text="Help – ik voel me alleen",
    width=30,
    command=lambda: messagebox.showinfo("❤️ Ik ben er!", "Je bent niet alleen. Bel Mara.")
).pack(pady=(30, 6))

affirmatie = random.choice(affirmaties)
affirmatie_frame = ttk.LabelFrame(home, text="✨ Dagelijkse affirmatie ✨", style="Custom.TLabelframe", padding=20)  # VISUEEL KADER
affirmatie_frame.pack(pady=60, padx=45, anchor="center", fill="x")

ttk.Label(
    affirmatie_frame,
    text=f"“{affirmatie}”",
    style="Custom.TLabel",
    wraplength=600,
    justify="center",
    font=("Helvetica Neue", 12, "italic"),
).pack()

# NOTE: info over app
def toon_info_popup():
    venster = tk.Toplevel()
    venster.title("Over deze app")
    center_window(venster, 400, 200)
    venster.configure(bg="#f9f9f9")

    ttk.Label(
        venster,
        text="© 2025\n\nGemaakt met liefde door Mara Janssen & June Sallou,\nvoor Naomi van der Weele.",
        style="Custom.TLabel", background="#f9f9f9",
        font=("Helvetica Neue", 10), justify="center"
    ).pack(expand=True, fill="both", padx=20, pady=20)

    ttk.Button(venster, text="Sluiten", command=venster.destroy).pack(pady=5)

ttk.Button(root, text="ℹ️", command=toon_info_popup, width=3).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

# PAGE: notitiepagina
notitie = pages["Notitie"]

ttk.Label(notitie, text="\n\n\nHoe voel je je vandaag?", style="Custom.TLabel").pack(pady=10)
stemming_keuze = tk.StringVar()
stemming_menu = ttk.Combobox(notitie, textvariable=stemming_keuze, values=moods, state="readononly")
stemming_menu.set(moods[0])
stemming_menu.pack()

ttk.Label(notitie, text="Wat heb je vandaag nodig?", style="Custom.TLabel").pack(pady=10)
behoefte_keuze = tk.StringVar()
behoefte_keuze.set(behoefte_opties[0])
behoefte_menu = ttk.Combobox(notitie, textvariable=behoefte_keuze, values=behoefte_opties, state="readonly")
behoefte_menu.pack()

ttk.Label(notitie, text="Wat voelde als een ankerplek?", style="Custom.TLabel").pack(pady=10)
ankerplek_entry = tk.Entry(notitie, width=50)
ankerplek_entry.pack()

ttk.Label(notitie, text="Wat leeft er in je?", style="Custom.TLabel").pack(pady=10)
gevoelstekst = tk.Text(notitie, height=15, width=70, wrap="word", font=("Georgia", 10))
gevoelstekst.pack()

def opslaan():
    gevoel = gevoelstekst.get("1.0", tk.END).strip()
    stemming = stemming_keuze.get()
    behoefte = behoefte_keuze.get()
    plek = ankerplek_entry.get().strip()

    if not gevoel:
        messagebox.showwarning("Leeg veld", "Vul eerst iets in.")
        return
    
    datum = datetime.now().strftime("%d-%m-%Y")
    tijd = datetime.now().strftime("%H:%M")
    mood_naam = stemming # direct gebruik, al gelabeld
    suggesties = genereer_suggesties(gevoel)

    entry = (
        f"{datum} {tijd}\n"
        f"Stemming: {stemming} ({mood_naam})\n"
        f"Behoefte vandaag: {behoefte}\n"
        f"Ankerplek: {plek if plek else '-'}\n"
        f"Gevoelens: {gevoel}\n"
        f"Suggesties:\n{suggesties}\n\n"
    )

    with open(BESTAND, "a", encoding="utf-8") as f:
        f.write(entry)
    
    suggesties_tekstvak.config(state=tk.NORMAL)
    suggesties_tekstvak.delete("1.0", tk.END)
    suggesties_tekstvak.insert(tk.END, suggesties)
    suggesties_tekstvak.config(state=tk.DISABLED)
    show_page("Suggesties")  # Toon suggestiepagina na opslaan

    gevoelstekst.delete("1.0", tk.END)
    ankerplek_entry.delete(0, tk.END)
    update_kalender()
    messagebox.showinfo("Opgeslagen", "Je notitie is opgeslagen.")

tk.Button(notitie, text="Opslaan", command=opslaan).pack(pady=10)
tk.Button(notitie, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack()

# PAGE: geschiedenis
geschiedenis = pages["Geschiedenis"]
ttk.Label(geschiedenis, text="Geschiedenis", style="Custom.TLabel").pack()
historieveld = tk.Text(geschiedenis, height=30, width=80, bg="#fff9f0", font=("Georgia", 10))
historieveld.pack()
tk.Button(geschiedenis, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack(pady=5)

def laad_dagboek():
       if not os.path.exists(BESTAND):
           return
       with open(BESTAND, "r", encoding="utf-8") as f:
            inhoud = f.read().strip()
            notities = inhoud.split("\n\n")
            notities.reverse()

            historieveld.config(state=tk.NORMAL)
            historieveld.delete("1.0", tk.END)
            historieveld.tag_config("label", font=("Helvetica Neue", 10, "bold"))

            for notitie in notities:
                regels = notitie.split("\n")
                for regel in regels:
                    if ":" in regel:
                        label, rest = regel.split(":", 1)
                        historieveld.insert(tk.END, f"{label}:", "label")
                        historieveld.insert(tk.END, f"{rest.strip()}\n")
                    else:
                        historieveld.insert(tk.END, regel + "\n")
                historieveld.insert(tk.END, "\n")

            historieveld.config(state=tk.DISABLED)

# PAGE: kalender
kalender = pages["Kalender"]
ttk.Label(kalender, text="Kalenderoverzicht", style="Custom.TLabel").pack(pady=40)
kalenderframe = ttk.Frame(kalender, style="Custom.TFrame")
kalenderframe.pack()
ttk.Button(kalender, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack(pady=40)

def update_kalender():
    # Reset
    for widget in kalenderframe.winfo_children():
        widget.destroy()

    # Huidige maand
    year = datetime.now().year
    month = datetime.now().month
    cal = calendar.monthcalendar(year, month)

    # Lees data met notities
    dagen = set()
    if os.path.exists(BESTAND):
        with open(BESTAND, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() and line[0].isdigit():
                    datum = line.split()[0]
                    d = datetime.strptime(datum, "%d-%m-%Y")
                    if d.year == year and d.month == month:
                        dagen.add(d.day)
        
    # Koptekst
    for i, dag in enumerate(["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]):
        tk.Label(kalenderframe, text=dag, width=6, font=("Georgia", 10, "bold"), bg="#d8cfc4").grid(row=0, column=i)

    # Dagen
    for r, week in enumerate(cal, start=1):
        for c, dag in enumerate(week):
            if dag == 0:
                tk.Label(kalenderframe, text="", width=6, bg="#f5f0e1").grid(row=r, column=c)  # STYLE: retro leeg vak
            else:
                kleur = "#a35638" if dag in dagen else "#fff9f0"  # STYLE: retro dagkleur
                btn = tk.Button(kalenderframe, text=str(dag), bg=kleur, width=6,
                                command=lambda d=dag: toon_notitie_van_dag(d))
                btn.grid(row=r, column=c)
        
def toon_notitie_van_dag(dag):
    dag_str = f"{dag:02d}-{datetime.now().month:02d}-{datetime.now().year}"
    output = ""
    if os.path.exists(BESTAND):
            with open(BESTAND, "r", encoding="utf-8") as f:
                inhoud = f.read()
                stukken = inhoud.strip().split("\n\n")
                for stuk in stukken:
                    if dag_str in stuk:
                        output += stuk + "\n\n"
    if output:
        messagebox.showinfo(f"Notitie van {dag_str}", output)
    else:
        messagebox.showinfo("Geen notitie", f"Er is geen notitie gevonden voor {dag_str}.")

# GUI maanstand
maanpagina = pages["MaanstandVandaag"]
ttk.Label(maanpagina, text="Stand van de Maan vandaag", style="Custom.TLabel", font=("Helvetica Neue", 14)).pack(pady=10)
maan_tekst = tk.StringVar()
ttk.Label(maanpagina, textvariable=maan_tekst, style="Custom.TLabel", justify="center", wraplength=500).pack(pady=10)

# Bereken actuele maanstand




# PAGE: Suggesties
suggestiepagina = pages["Suggesties"]
ttk.Label(suggestiepagina, text="Suggesties voor jouw welzijn", style="Custom.TLabel").pack(pady=20)
suggesties_tekstvak = tk.Text(suggestiepagina, height=15, width=70, wrap="word", font=("Helvetica Neue", 11), bg="#fff9f0")
suggesties_tekstvak.pack(pady=10)
tk.Button(suggestiepagina, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack(pady=10)

# START: eerste scherm
show_page("Start")
root.mainloop()


