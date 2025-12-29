import ttkbootstrap as ttk


class BaseLayout(ttk.Frame):
    def __init__(self, master, title='Van Mex Comercial'):
        super().__init__(master)

        #header
        self.header = ttk.Frame(self, bootstyle='primary')
        self.header.pack(fill="x")
 
        ttk.Label(
            self.header,
            text='title',
            bootstyle='inverse-primary',
            font=('Segoe UI', 14, 'bold'),
            padding=10,
        ).pack(side='left')

        #conteudo
        self.content = ttk.Frame(self, padding=15)
        self.content.pack(fill='both', expand=True)

         #footer
        self.footer = ttk.Frame(self, bootstyle="light")
        self.footer.pack(fill="x")

        ttk.Label(
            self.footer,
            text="© Sistema Van Mex Comercial",
            font=("Segoe UI", 9),
            padding=5
        ).pack(side="right")
