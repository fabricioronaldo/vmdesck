import ttkbootstrap as ttk

class MainView(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)

        ttk.Label(self, text="Menu Principal", font=("Helvetica", 16)).pack(pady=20)

        ttk.Button(
            self, text="Clientes",
            command=lambda: controller.show_frame("ClienteView")
        ).pack(pady=5)
