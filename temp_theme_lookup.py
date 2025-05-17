import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style()
style.theme_use("clam")

# Ophalen van de standaard achtergrondkleur van een Frame
frame_bg = style.lookup("TFrame", "background")

# Maak een eigen stijl die exact deze kleur gebruikt
style.configure("Custom.TFrame", background=frame_bg)

frame = ttk.Frame(root, style="Custom.TFrame", padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Dit is een label in een frame").pack(pady=10)

root.mainloop()