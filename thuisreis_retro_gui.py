import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random
import os
import calendar
import math


BESTAND = "thuireis_journal.txt"

affirmaties = [
    "Ik mag het langzaam aan doen vandaag.",
    "Ik ben precies waar ik nu moet zijn.",
    "Mijn gevoel mag er helemaal zijn.",
    "Adem in rust, adem uit spanning.",
    "Ik ben veilig in mijn lichaam.",
    "Alles komt op het juiste moment.",
    "Ik hoef niets te forceren.",
    "Mijn huis is een verlengstuk van mijn innerlijke wereld.",
    "Ik geef mezelf toestemming om te landen.",
    "Ik ben in proces, en dat is genoeg.",
    "Ik mag ruimte innemen.",
    "Mijn adem brengt me altijd terug naar hier.",
    "Ik vertrouw op het ritme van mijn leven.",
    "Elke dag vind ik een beetje meer mijn plek.",
    "Ik mag thuiskomen in mezelf.",
    "Ik ben zacht voor mezelf, ook als het moeilijk is.",
    "Ik mag loslaten wat niet meer past.",
    "Ik creëer veiligheid van binnenuit.",
    "Ik hoef het niet alleen te doen.",
    "Ik ben verbonden, ook als ik me alleen voel.",
    "Ik ben welkom in deze wereld, precies zoals ik ben.",
    "Mijn energie is kostbaar en verdient zorg.",
    "Ik geef mezelf liefde zonder voorwaarden.",
    "Ik laat verwachtingen los en kies voor zachtheid.",
    "Ik luister naar wat mijn lichaam nodig heeft.",
    "Ik ben niet achter of te laat, ik beweeg op mijn tempo.",
    "Elke ademhaling is een nieuw begin.",
    "Ik mag rust nemen zonder me schuldig te voelen.",
    "Thuis is iets dat ik in mij draag.",
    "Mijn emoties zijn mijn kompas, geen bedreiging.",
    "Ik ben krachtig in mijn kwetsbaarheid.",
    "Mijn stilte heeft waarde.",
    "Ik mag groeien, zelfs als dat langzaam gaat.",
    "Ik ben goed genoeg, nu al.",
    "Ik hoef niet alles te weten om verder te gaan.",
    "Ik adem liefde in en spanning uit.",
    "Ik creëer ruimte voor mijn verdriet én mijn vreugde.",
    "Ik ben zacht én sterk tegelijk.",
    "Vertrouwen groeit met elke stap die ik zet.",
    "Ik draag mijn verleden met respect en loop vooruit.",
    "Wat ik voel is belangrijk.",
    "Mijn tempo is heilig.",
    "Ik ben thuis in dit moment.",
    "Ik kies vandaag voor rust in plaats van haast.",
    "Ik hoef het niet te fixen, alleen aanwezig te zijn.",
    "Ik ben een mens in ontwikkeling, en dat is prachtig.",
    "Mijn gevoelens hebben bestaansrecht.",
    "Ik omarm het onbekende met nieuwsgierigheid.",
    "Ik mag nieuwe gewoonten creëren die mij voeden.",
    "Ik ben veilig om te voelen, te rouwen, te helen."
]

moods = {
    "😊 Blij": "blij",
    "😔 Verdrietig": "droevig",
    "😐 Neutraal": "neutraal",
    "😖 Gestresst": "gestrest",
    "😌 Kalm": "kalm",
    "🥺 Kwetsbaar": "kwetsbaar",
    "🤍 Vol liefde": "liefdevol"
}

behoefte_opties = ["rust", "energie", "richting", "liefde", "steun", "warmte"]

emotionele_thema_suggesties = {
    "kwetsbaarheid": {
        "woorden": ["kwetsbaar", "geraakt", "gevoelig", "open"],
        "suggestie": "Doe een hartopenende houding zoals Anahata-asana."
    },
    "ontheemding": {
        "woorden": ["ontheemd", "vreemd", "geen plek", "niet thuis"],
        "suggestie": "Maak een klein altaartje met iets van je Amsterdamse thuis (Mara) en iets van hier."
    },
    "rusteloosheid": {
        "woorden": ["rusteloos", "onrustig", "druk in hoofd"],
        "suggestie": "Probeer yoga nidra, yin yoga of een bodyscan voor diepe ontspanning."
    },
    "vermoeidheid": {
        "woorden": ["moe", "uitgeput", "leeg", "futloos"],
        "suggestie": "Sluit je ogen en leg je handen op je onderbuik. Adem zacht in richting je handen, alsof je je eigen bron opnieuw vult. Blijf hier minstens 5 ademhalingen. Je hoeft niets te doen, alleen te zijn."
    },
    "eenzaamheid": {
        "woorden": ["eenzaam", "alleen", "verlaten"],
        "suggestie": "Breng je handen op je hart en herinner jezelf: je bent verbonden - met jezelf en met Mara."
    },
    "angst": {
        "woorden": ["angstig", "bang", "bezorgd", "nerveus"],
        "suggestie": "Adem in door je neus, uit met een zachte zucht. Herhaal 5x met gesloten ogen."
    },
    "overprikkeling": {
        "woorden": ["overprikkeld", "vol hoofd", "te veel", "druk"],
        "suggestie": "Sluit je ogen, masseer zacht je slapen met warme olie, en trek je even terug."
    },
    "verwarring": {
        "woorden": ["verwarring", "verward", "geen richting"],
        "suggestie": "Schrijf 5 minuten zonder stoppen – laat het stromen."
    },
    "boosheid": {
        "woorden": ["boos", "woede", "frustratie", "irritatie"],
        "suggestie": "Schrijf een brief die je niet hoeft te versturen – uit alles zonder filter."
    },
    "stilte": {
        "woorden": ["stil", "stilte", "weinig", "geruisloos"],
        "suggestie": "Omarm de stilte – neem 10 minuten zonder input en voel je eigen ritme."
    },
    "dankbaarheid": {
        "woorden": ["dankbaar", "waardering", "voldoening"],
        "suggestie": "Leg een steen of voorwerp op je altaar als symbool van dankbaarheid - of schrijf dit moment in een notitieboek ter herinnering."
    },
    "klein voelen": {
        "woorden": ["klein", "weggedrukt", "onzichtbaar"],
        "suggestie": "Rol jezelf op in Child’s Pose en adem alsof je gedragen wordt door de aarde."
    },
    "onzekerheid": {
        "woorden": ["onzeker", "twijfel", "zelftwijfel", "niet goed genoeg"],
        "suggestie": "Sta in Tadasana en voel je voeten stevig in de aarde."
    }, 

    "spijt": {
        "woorden": ["spijt", "had ik maar", "ik wou dat", "te laat", "spijtig", "jammer", "helaas"],
        "suggestie": "Schrijf een brief aan je vroegere zelf. Zeg alleen wat je nu weet, zonder oordeel. Je hoeft de brief niet te bewaren – laat het een vorm van loslaten zijn."
    },

    "keuzestress": {
        "woorden": ["keuzestress", "niet kiezen", "twijfel", "vastlopen", "knoop doorhakken", "keuzes"],
        "suggestie": "Leg je hand op je hart en stel jezelf de vraag: 'Als ik niets hoef te bewijzen, wat voelt dan licht?' Geef het antwoord tijd – je lichaam weet het vaak eerder dan je hoofd."
    },

    "geen richting": {
        "woorden": ["geen richting", "verdwaald", "ik weet het niet", "zoekend", "geen idee"],
        "suggestie": "Pak drie willekeurige voorwerpen en leg ze om je heen. Geef elk voorwerp een betekenis. Wat zegt dit mini-orakel vandaag tegen jou? Soms ontstaat richting door spel en toeval."
    },

    "schuldgevoel": {
        "woorden": ["schuld", "schuldgevoel", "had ik anders moeten doen", "het is mijn fout", "schuldig"],
        "suggestie": "Leg beide handen op je hart en fluister zacht: 'Ik mag leren. Ik mag mens zijn. Ik ben goed zoals ik ben.' Herhaal dit drie keer, langzaam. Laat je adem zachter worden. Schuld lost niet op door straf, maar door zachtheid."
    }
}

def genereer_suggesties(tekst):
    gevonden = []
    tekst_lc = tekst.lower()
    for thema in emotionele_thema_suggesties.values():
        if any(woord in tekst_lc for woord in thema["woorden"]):
            gevonden.append(f"- {thema['suggestie']}")
    return "\n".join(gevonden) if gevonden else "Geen specifieke suggesties gevonden."

# NOTE: hoofdvenster en stijl
root = tk.Tk()
root.title("🕰️ Thuisreis – Naomi's Journey Home")
root.geometry("700x700")
root.configure(bg="#f5f0e1")

# NOTE: maak container voor paginawisseling
container = tk.Frame(root, bg="#f5f0e1")
container.pack(fill="both", expand=True)

# NOTE: opslaan alle frames in dict
pages = {}

for page_name in ["Start", "Notitie", "Geschiedenis", "Kalender", "MaanstandVandaag", "Suggesties"]:
    frame = tk.Frame(container, bg="#f5f0e1")
    frame.grid(row=0, column=0, sticky="nsew")
    pages[page_name] = frame

# FUNCTION: pagina wisselen
def show_page(page_name):
    pages[page_name].tkraise()

# PAGE: startmenu
home = pages["Start"]
tk.Label(home, text="Welkom bij Naomi's Thuisreis", font=("Georgia", 16, "bold"), bg="#f5f0e1").pack(pady=30)

# Introtekst
tk.Label(
    home,
    text=(
        "Welkom in jouw persoonlijke dagboekruimte. 🤍\n\n"
        "Deze app draait alleen lokaal, dus niemand kan hierbij. Hier kun je veilig schrijven over hoe je je voelt in de eerste maanden waarin je je nieuwe plek ontdekt. Ik hoop dat je zo altijd rust kunt vinden in een dagelijkse affirmatie, en steun kunt ontvangen via goedbedoelde suggesties en tips (of eventueel de maanstand). Neem je tijd, adem diep, en laat dit een plek zijn waar je steeds opnieuw mag thuiskomen."
    ),
    font=("Georgia", 11),
    wraplength=600,
    justify="center",
    bg="#f5f0e1",
    fg="#4a3f35"
).pack(pady=(0, 30))

# Groepeer knoppen in een frame
button_frame = tk.Frame(home, bg="#f5f0e1")
button_frame.pack()

# Standaard knopstijl
knop_breedte = 30
knop_stijl = {"font": ("Georgia", 12, "italic"), "bg": "#a35638", "fg": "white", "width": knop_breedte}

tk.Button(button_frame, text="Schrijf een dagboeknotitie", **knop_stijl, command=lambda: show_page("Notitie")).pack(pady=5)
tk.Button(button_frame, text="Bekijk geschiedenis", **knop_stijl, command=lambda: [laad_dagboek(), show_page("Geschiedenis")]).pack(pady=5)
tk.Button(button_frame, text="Kalender bekijken", **knop_stijl, command=lambda: [update_kalender(), show_page("Kalender")]).pack(pady=5)
tk.Button(
    button_frame,
    text="Stand van de Maan",
    **knop_stijl,
    command=lambda: show_page("MaanstandVandaag")
).pack(pady=5)
tk.Button(
    button_frame,
    text="Help – ik voel me alleen",
    font=("Georgia", 11, "italic"),
    bg="#b02e2e", fg="white", width=30,
    command=lambda: messagebox.showinfo("❤️ Ik ben er!", "Je bent niet alleen. Bel Mara.")
).pack(pady=(30, 6))

affirmatie = random.choice(affirmaties)
affirmatie_frame = tk.Frame(home, bg="#efe6d3", pady=20, padx=10, bd=2, relief="ridge")  # VISUEEL KADER
affirmatie_frame.pack(pady=60, padx=45, fill="x")

tk.Label(
    affirmatie_frame,
    text="✨ Dagelijkse affirmatie ✨",
    font=("Georgia", 12, "bold"),
    fg="#4a3f35",
    bg="#efe6d3"
).pack()

tk.Label(
    affirmatie_frame,
    text=f"“{affirmatie}”",
    wraplength=600,
    justify="center",
    font=("Georgia", 12, "italic"),
    fg="#3c2f2f",
    bg="#efe6d3"
).pack()

# PAGE: notitiepagina
notitie = pages["Notitie"]

tk.Label(notitie, text="\n\n\nHoe voel je je vandaag?", bg="#f5f0e1", font=("Georgia", 10)).pack(pady=10)
stemming_keuze = tk.StringVar()
stemming_keuze.set("😐")
tk.OptionMenu(notitie, stemming_keuze, *moods.keys()).pack()

tk.Label(notitie, text="Wat heb je vandaag nodig?", bg="#f5f0e1", font=("Georgia", 10)).pack(pady=10)
behoefte_keuze = tk.StringVar()
behoefte_keuze.set(behoefte_opties[0])
tk.OptionMenu(notitie, behoefte_keuze, *behoefte_opties).pack()

tk.Label(notitie, text="Wat voelde als een ankerplek?", bg="#f5f0e1", font=("Georgia", 10)).pack(pady=10)
ankerplek_entry = tk.Entry(notitie, width=50)
ankerplek_entry.pack()

tk.Label(notitie, text="💬 Wat leeft er in je?", bg="#ede8de", font=("Georgia", 10)).pack(pady=10)
gevoelstekst = tk.Text(notitie, height=15, width=70, wrap="word", font=("Georgia", 10))
gevoelstekst.pack()

def opslaan():
    gevoel = gevoelstekst.get("1.0", tk.END).strip()
    stemming = stemming_keuze.get()
    behoefte = behoefte_keuze.get()
    plek = ankerplek_entry.get().strip()

    if not gevoel:
        messagebox.showwarning("Leeg veld", "Vul eerst je gevoelens in.")
        return
    
    datum = datetime.now(). strftime("%d-%m-%Y")
    tijd = datetime.now().strftime("%H:%M")
    mood_naam = moods.get(stemming, "onbekend")
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

tk.Button(notitie, text="Opslaan", font=("Georgia", 11, "bold"), bg="#a35638", fg="white", command=opslaan).pack(pady=10)
tk.Button(notitie, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack()

# PAGE: geschiedenis
geschiedenis = pages["Geschiedenis"]
tk.Label(geschiedenis, text="📖 Geschiedenis", font=("Georgia", 14), bg="#f5f0e1").pack()
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
            historieveld.tag_config("label", font=("Georgia", 10, "bold"))

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
tk.Label(kalender, text="📅 Kalenderoverzicht", font=("Georgia", 14), bg="#f5f0e1").pack(pady=40)
kalenderframe = tk.Frame(kalender, bg="#f5f0e1")
kalenderframe.pack()
tk.Button(kalender, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack(pady=40)

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


# Bereken actuele maanstand
def bereken_maanfase_en_teken():
    # Gebaseerd op algoritme van John Walker / simplified lunation
    now = datetime.utcnow()
    year, month = now.year, now.month
    day = now.day + now.hour / 24 + now.minute / 1440

    if month < 3:
        year -= 1
        month += 12

    a = int(year / 100)
    b = 2 - a + int(a / 4)
    c = int(365.25 * year)
    d = int(30.6001 * (month + 1))
    days_since_new = c + d + day + b - 694039.09
    lunation = days_since_new % 29.53058867

    # ➕ Nieuw: bepaal of de maan aan het wassen of afnemen is
    if lunation < 14.765:  # voor volle maan
        richting = "wassende"
    else:
        richting = "afnemende"

    fase = (lunation / 29.53058867) * 100

    if fase < 1 or fase > 99:
        fase_naam = "🌑 Nieuwe maan"
    elif fase < 25:
        fase_naam = f"🌒 {richting} sikkel"
    elif fase < 50:
        fase_naam = f"🌓 Eerste kwartier" if richting == "wassende" else "🌗 Laatste kwartier"
    elif fase < 75:
        fase_naam = f"🌔 {richting} maan"
    else:
        fase_naam = "🌕 Volle maan"

    # Geschatte positie (zelfde benadering als eerder)
    positie_graden = (lunation * 360 / 29.53058867) % 360
    tekens = [
        "♈ Ram", "♉ Stier", "♊ Tweelingen", "♋ Kreeft",
        "♌ Leeuw", "♍ Maagd", "♎ Weegschaal", "♏ Schorpioen",
        "♐ Boogschutter", "♑ Steenbok", "♒ Waterman", "♓ Vissen"
    ]
    teken_index = int(positie_graden // 30)
    teken = tekens[teken_index]
    graden_in_teken = int(positie_graden % 30)

    return fase_naam, f"{graden_in_teken}° {teken}"

# GUI maanstand
maanpagina = pages["MaanstandVandaag"]

tk.Label(maanpagina, text="🌙 Stand van de Maan vandaag", font=("Georgia", 14), bg="#f5f0e1").pack(pady=10)

maan_tekst = tk.StringVar()
tk.Label(maanpagina, textvariable=maan_tekst, font=("Georgia", 12), justify="center", bg="#f5f0e1").pack(pady=10)

def toon_maanstand():
    fase, positie = bereken_maanfase_en_teken()
    maan_tekst.set(f"{fase}\nMaan staat op {positie}")

tk.Button(maanpagina, text="🔄 Vernieuw", command=toon_maanstand).pack(pady=5)
tk.Button(maanpagina, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack(pady=10)

toon_maanstand()

# PAGE: Suggesties
suggestiepagina = pages["Suggesties"]
tk.Label(suggestiepagina, text="🤲 Suggesties voor jouw welzijn", font=("Georgia", 14), bg="#f5f0e1").pack(pady=20)
suggesties_tekstvak = tk.Text(suggestiepagina, height=15, width=70, wrap="word", font=("Georgia", 10), bg="#fff9f0")
suggesties_tekstvak.pack(pady=10)
tk.Button(suggestiepagina, text="🏠 Terug naar menu", command=lambda: show_page("Start")).pack(pady=10)

# START: eerste scherm
show_page("Start")
root.mainloop()

