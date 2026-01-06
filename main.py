import tkinter as tk
from tkinter import messagebox
import random

# --- CONFIGURATION (Jetstorm Theme) ---
THEME_BG = "#050510"        # Dark Space
GRID_COLOR = "#102a43"      # Faint Grid
STAR_COLOR = "#ffffff"
CYAN_COLOR = "#00FFFF"      # Neon Cyan
YELLOW_COLOR = "#FFD700"    # Gold
TEXT_COLOR = "#E0E0E0"

# --- ZODIAC DATA ---
ZODIAC_INFO = {
    "Capricorn": {"symbol": "♑", "element": "Earth", "lucky": "4, 8, 13", "trait": "Ambitious & Disciplined"},
    "Aquarius":  {"symbol": "♒", "element": "Air",   "lucky": "7, 11",    "trait": "Innovative & Original"},
    "Pisces":    {"symbol": "♓", "element": "Water", "lucky": "3, 9",     "trait": "Artistic & Emotional"},
    "Aries":     {"symbol": "♈", "element": "Fire",  "lucky": "1, 9",     "trait": "Bold & Courageous"},
    "Taurus":    {"symbol": "♉", "element": "Earth", "lucky": "2, 6",     "trait": "Reliable & Patient"},
    "Gemini":    {"symbol": "♊", "element": "Air",   "lucky": "5, 7",     "trait": "Curious & Adaptable"},
    "Cancer":    {"symbol": "♋", "element": "Water", "lucky": "2, 3",     "trait": "Intuitive & Caring"},
    "Leo":       {"symbol": "♌", "element": "Fire",  "lucky": "1, 4, 6",  "trait": "Confident & Leader"},
    "Virgo":     {"symbol": "♍", "element": "Earth", "lucky": "5, 14",    "trait": "Analytical & Kind"},
    "Libra":     {"symbol": "♎", "element": "Air",   "lucky": "6, 15",    "trait": "Diplomatic & Fair"},
    "Scorpio":   {"symbol": "♏", "element": "Water", "lucky": "8, 11",    "trait": "Passionate & Resourceful"},
    "Sagittarius":{"symbol": "♐", "element": "Fire",  "lucky": "3, 7, 9",  "trait": "Optimistic & Honest"}
}

class ZodiacMaster:
    def __init__(self, root):
        self.root = root
        self.root.title("Zodiac Master - Project Z")
        self.root.geometry("500x700")
        self.root.resizable(False, False)
        
        # Canvas Background
        self.canvas = tk.Canvas(root, width=500, height=700, bg=THEME_BG, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.draw_space_bg()

        # Title Section (Yellow Bars + Cyan Text)
        self.canvas.create_rectangle(80, 50, 420, 60, fill=YELLOW_COLOR, outline="")
        self.canvas.create_text(250, 85, text="ZODIAC MASTER", fill=CYAN_COLOR, font=("Impact", 32))
        self.canvas.create_text(250, 120, text="✨ PROJECT Z: THE FINALE ✨", fill="white", font=("Consolas", 10))

        # Inputs
        self.create_inputs()

        # Result Area
        self.result_sign_id = self.canvas.create_text(250, 320, text="", fill=YELLOW_COLOR, font=("Verdana", 35, "bold"))
        self.result_symbol_id = self.canvas.create_text(250, 400, text="", fill="white", font=("Segoe UI Symbol", 60))
        self.result_details_id = self.canvas.create_text(250, 520, text="", fill="white", font=("Consolas", 12), justify="center")

        # Footer
        self.canvas.create_text(250, 660, text="Built with Python 🐍 | Developer: Laxmi Sanas", fill="#555", font=("Consolas", 9))

    def draw_space_bg(self):
        # Stars
        for _ in range(100):
            x = random.randint(0, 500)
            y = random.randint(0, 700)
            s = random.randint(1, 2)
            self.canvas.create_oval(x, y, x+s, y+s, fill=STAR_COLOR, outline="")
        # Grid
        for i in range(0, 800, 50):
            self.canvas.create_line(0, i, 500, i, fill=GRID_COLOR, width=1)
            self.canvas.create_line(i, 0, i, 700, fill=GRID_COLOR, width=1)

    def create_inputs(self):
        lbl_style = {"bg": THEME_BG, "fg": TEXT_COLOR, "font": ("Arial", 10)}
        entry_style = {"bg": "#111", "fg": "white", "insertbackground": "white", "justify": "center", "font": ("Arial", 12)}

        tk.Label(self.root, text="Day (1-31):", **lbl_style).place(x=100, y=160)
        self.entry_day = tk.Entry(self.root, **entry_style)
        self.entry_day.place(x=100, y=185, width=80, height=30)

        tk.Label(self.root, text="Month (1-12):", **lbl_style).place(x=220, y=160)
        self.entry_month = tk.Entry(self.root, **entry_style)
        self.entry_month.place(x=220, y=185, width=80, height=30)

        btn = tk.Button(self.root, text="REVEAL 🔮", bg=CYAN_COLOR, fg="black", font=("Arial", 11, "bold"), cursor="hand2", command=self.calculate_zodiac)
        btn.place(x=320, y=183, width=100, height=34)

    def get_sign(self, day, month):
        if month == 12: return 'Sagittarius' if (day < 22) else 'Capricorn'
        elif month == 1: return 'Capricorn' if (day < 20) else 'Aquarius'
        elif month == 2: return 'Aquarius' if (day < 19) else 'Pisces'
        elif month == 3: return 'Pisces' if (day < 21) else 'Aries'
        elif month == 4: return 'Aries' if (day < 20) else 'Taurus'
        elif month == 5: return 'Taurus' if (day < 21) else 'Gemini'
        elif month == 6: return 'Gemini' if (day < 21) else 'Cancer'
        elif month == 7: return 'Cancer' if (day < 23) else 'Leo'
        elif month == 8: return 'Leo' if (day < 23) else 'Virgo'
        elif month == 9: return 'Virgo' if (day < 23) else 'Libra'
        elif month == 10: return 'Libra' if (day < 23) else 'Scorpio'
        elif month == 11: return 'Scorpio' if (day < 22) else 'Sagittarius'
        return None

    def calculate_zodiac(self):
        try:
            d = int(self.entry_day.get())
            m = int(self.entry_month.get())
            if not (1 <= m <= 12) or not (1 <= d <= 31):
                messagebox.showerror("Error", "Invalid Date!")
                return
            
            sign = self.get_sign(d, m)
            if sign:
                data = ZODIAC_INFO[sign]
                self.canvas.itemconfig(self.result_sign_id, text=sign.upper())
                self.canvas.itemconfig(self.result_symbol_id, text=data['symbol'])
                self.canvas.itemconfig(self.result_details_id, text=f"Element: {data['element']} ⚡\nLucky: {data['lucky']} 🎲\nTrait: {data['trait']} ✨")
        except ValueError:
            messagebox.showerror("Error", "Numbers only!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ZodiacMaster(root)
    root.mainloop()