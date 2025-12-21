from ttkbootstrap.constants import *
import ttkbootstrap as tb


def nova_tela():
  janela_pregao = tb.Toplevel(root.root)
  janela_pregao.title('Van Mex Pegrões')
  janela_pregao.geometry('300x200')

  tb.Label(janela_pregao, text='Pregões Cadastrados', font=('Helvetica', 28), bootstyle='defout').pack(pady=20)
  tb.Button(janela_pregao, text='Fechar', bootstyle='danger', command=janela_pregao.destroy).pack()