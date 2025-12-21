from ttkbootstrap.constants import *
import ttkbootstrap as tb
from pregao import nova_tela

root = tb.Window(themename='superhero')
#Configuração da Janela Principal
root.title('Van Mex Comercial')
root.geometry('700x400')
root.minsize(width=500, height=300)

h1_title = tb.Label(text='Menu Principal', font=('Helvetica', 28), bootstyle='defout')
h1_title.pack(pady=20)

b1 = tb.Button(root, text='Pregão', bootstyle='SUCCESS', command=nova_tela)
b1.pack(side=LEFT, padx=5, pady=10)
  
root.mainloop()