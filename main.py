import ttkbootstrap as ttk
from views.main_view import MainView
from views.cliente_view import ClienteView
from database.db import init_db

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="flatly")
        self.title("Sistema MVC Desktop")
        self.geometry("600x400")

        init_db()

        self.frames = {}
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        for View in (MainView, ClienteView):
            frame = View(container, self)
            self.frames[View.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainView")

    def show_frame(self, name):
        self.frames[name].tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
