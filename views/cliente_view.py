import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from views.base_view import BaseView
from views.layout import BaseLayout
from views.sidebar import Sidebar
from controllers.cliente_controller import ClienteController


class ClienteView(BaseView):

    def __init__(self, master, controller):
        super().__init__(master)

        self.app_controller = controller
        self.controller = ClienteController()
        self.cliente_id = None

        # Layout principal
        layout = ttk.Frame(self)
        layout.pack(fill="both", expand=True)

        Sidebar(layout, controller).pack(side="left", fill="y")

        main = BaseLayout(layout, title="Cadastro de Clientes")
        main.pack(side="right", fill="both", expand=True)
        content = main.content

        # Formulário
        form = ttk.Labelframe(content, text="Dados do Cliente", padding=15)
        form.pack(fill="x")

        ttk.Label(form, text="Nome").grid(row=0, column=0, sticky="w")
        ttk.Label(form, text="Email").grid(row=1, column=0, sticky="w")

        self.nome_entry = ttk.Entry(form, width=40)
        self.email_entry = ttk.Entry(form, width=40)

        self.nome_entry.grid(row=0, column=1, padx=10, pady=5)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botões
        botoes = ttk.Frame(content)
        botoes.pack(pady=10)

        ttk.Button(
            botoes, text="Salvar", bootstyle="success",
            command=self.salvar
        ).pack(side="left", padx=5)

        ttk.Button(
            botoes, text="Excluir", bootstyle="danger",
            command=self.excluir
        ).pack(side="left", padx=5)

        # Tabela
        self.tree = ttk.Treeview(
            content, columns=("id", "nome", "email"), show="headings", height=10
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("email", text="Email")
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.selecionar)

        self.atualizar_lista()

    # ======================
    # MÉTODOS DA VIEW
    # ======================

    def salvar(self):
        nome = self.nome_entry.get()
        email = self.email_entry.get()

        if self.cliente_id:
            sucesso, msg = self.controller.atualizar(
                self.cliente_id, nome, email
            )
        else:
            sucesso, msg = self.controller.salvar(nome, email)

        if sucesso:
            Messagebox.show_info(msg, title="Sucesso")
            self.limpar_form()
            self.atualizar_lista()
        else:
            Messagebox.show_error(msg, title="Erro")

    def excluir(self):
        if not self.cliente_id:
            Messagebox.show_warning("Selecione um cliente.", title="Aviso")
            return

        self.controller.excluir(self.cliente_id)
        Messagebox.show_info("Cliente excluído.", title="Sucesso")
        self.limpar_form()
        self.atualizar_lista()

    def selecionar(self, event):
        item = self.tree.selection()
        if not item:
            return

        valores = self.tree.item(item)["values"]
        self.cliente_id = valores[0]

        self.nome_entry.delete(0, "end")
        self.email_entry.delete(0, "end")

        self.nome_entry.insert(0, valores[1])
        self.email_entry.insert(0, valores[2])

    def atualizar_lista(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for cliente in self.controller.listar_clientes():
            self.tree.insert("", "end", values=cliente)

    def limpar_form(self):
        self.cliente_id = None
        self.nome_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
