import ttkbootstrap as ttk

class Sidebar(ttk.Frame):
    def __init__(self, master, controller):
        super().__init__(master, bootstyle="secondary")
        self.controller = controller

        ttk.Label(
            self,
            text="Menu",
            bootstyle="inverse-secondary",
            font=("Segoe UI", 12, "bold"),
            padding=10
        ).pack(fill="x")

        ttk.Button(
            self, text="Clientes",
            bootstyle="secondary",
            command=lambda: controller.show_frame("ClienteView")
        ).pack(fill="x", padx=10, pady=5)

        ttk.Button(
            self, text="Produtos",
            bootstyle="secondary"
        ).pack(fill="x", padx=10, pady=5)

        ttk.Button(
            self, text="Pregão",
            bootstyle="secondary"
        ).pack(fill="x", padx=10, pady=5)
