from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename='superhero')

root.title('Van Mex Comercial')
root.geometry('500x350')


h1_title = tb.Label(text='Menu Principal', font=('Helvetica', 28), bootstyle='defout')
h1_title.pack(pady=20)

b1 = tb.Button(root, text='Pregão', bootstyle='SUCCESS')
b1.pack(side=LEFT, padx=5, pady=10)

root.mainloop()