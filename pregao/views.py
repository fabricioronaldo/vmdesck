from ttkbootstrap.constants import *
import ttkbootstrap as tb


class PregaoView(tb.Window):
  def __init__(self, controller):
    super().__init__()
    
    self.controller = controller
    
    self.title('Van Mex Pregões')
    self.geometry('700x500')
    
    tb.Label(self, text='Pregões Cadastrados', font=('Helvetica', 28), bootstyle='defout').pack(pady=20)
    tb.Button(self, text='Fechar', bootstyle='danger', command=self.destroy).pack()  
    
   
