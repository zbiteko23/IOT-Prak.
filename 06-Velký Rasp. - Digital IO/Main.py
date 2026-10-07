from gpiozero import LED
from tkinter import *

led = LED(17)

okno = Tk()

Button(okno, text="ZAPNOUT", command=led.on).pack()
Button(okno, text="VYPNOUT", command=led.off).pack()

okno.mainloop()