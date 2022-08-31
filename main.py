from tkinter import *

main = Tk() # main window
main.title("디지털 교과서 - 학생용")
main.attributes('-fullscreen', True)

introduce_label = Label(main, text='디지털 교과서')
introduce_label.config(font=('맑은 고딕', 40))
introduce_label.pack()

main.mainloop()