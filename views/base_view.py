import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class BaseView(ttk.Frame):

    def mostrar_erro(self, mensagem):
        Messagebox.show_error(message=mensagem, title="Erro")

    def mostrar_sucesso(self, mensagem):
        Messagebox.show_info(message=mensagem, title="Sucesso")

    def limpar_entries(self, *entries):
        for entry in entries:
            entry.delete(0, "end")
