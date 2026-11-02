import tkinter as tk
from gpiozero import LED, Button
 
led = LED(17)
tlacitko = Button(27, bounce_time=0.05)
 
# Fyzické tlačítko přepíná výstup
tlacitko.when_pressed = led.toggle
 
okno = tk.Tk()
okno.title("Ovládání výstupu")
okno.geometry("300x220")
 
stav = tk.Label(okno, text="", font=("Arial", 20, "bold"), width=12, height=2)
stav.pack(pady=10)
 
tk.Button(okno, text="ZAPNOUT", font=("Arial", 14), bg="#4caf50", fg="white",
          command=led.on).pack(fill="x", padx=20, pady=4)
tk.Button(okno, text="VYPNOUT", font=("Arial", 14), bg="#f44336", fg="white",
          command=led.off).pack(fill="x", padx=20, pady=4)
 
def aktualizuj():
    # Čte skutečný stav výstupu, takže se okno změní i po stisku fyzického tlačítka
    if led.is_lit:
        stav.config(text="ZAPNUTO", bg="#c8f7c5")
    else:
        stav.config(text="VYPNUTO", bg="#f7c5c5")
    okno.after(100, aktualizuj)
 
aktualizuj()
okno.mainloop()