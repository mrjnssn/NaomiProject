
def get_affirmations(filename):
    affirmaties = []
    file = open(filename, "r")
    for line in file:
        affirmaties.append(line)
    return affirmaties

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



def convert_days_to_dhm(days_float):
    # Get the integer part as full days
    days = int(days_float)

    # Get the fractional part and convert to hours
    fractional_day = days_float - days
    total_hours = fractional_day * 24
    hours = int(total_hours)

    # Get the remaining fraction and convert to minutes
    fractional_hour = total_hours - hours
    minutes = int(fractional_hour * 60)

    return days, hours, minutes