from gpiozero import PWMLED
from tkinter import *

led = PWMLED(17)

okno = Tk()

def jas(x):
    led.value = int(x) / 100

Scale(okno, from_=0, to=100,
      command=jas).pack()

okno.mainloop()