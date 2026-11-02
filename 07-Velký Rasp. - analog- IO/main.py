import tkinter as tk
from gpiozero import PWMOutputDevice
 
bzucak = PWMOutputDevice(18, frequency=1000, initial_value=0)
 
okno = tk.Tk()
okno.title("Analogový výstup (PWM)")
okno.geometry("340x300")
 
def nastav_frekvenci(v):
    bzucak.frequency = int(float(v))
 
def nastav_hlasitost(v):
    bzucak.value = float(v) / 100   # střída PWM 0 až 1
 
tk.Label(okno, text="Frekvence (Hz)", font=("Arial", 12)).pack(pady=(15, 0))
frek = tk.Scale(okno, from_=100, to=4000, orient="horizontal", length=280,
                command=nastav_frekvenci)
frek.set(1000)
frek.pack()
 
tk.Label(okno, text="Výkon / střída (%)", font=("Arial", 12)).pack(pady=(15, 0))
vykon = tk.Scale(okno, from_=0, to=50, orient="horizontal", length=280,
                 command=nastav_hlasitost)
vykon.set(0)
vykon.pack()
 
def ticho():
    vykon.set(0)
    bzucak.off()
 
tk.Button(okno, text="TICHO", font=("Arial", 14), bg="#f44336", fg="white",
          command=ticho).pack(fill="x", padx=20, pady=20)
 
okno.protocol("WM_DELETE_WINDOW", lambda: (bzucak.off(), okno.destroy()))
okno.mainloop()