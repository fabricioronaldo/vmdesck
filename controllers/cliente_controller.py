from models.cliente_model import ClienteModel

class ClienteController:

    def listar_clientes(self):
        return ClienteModel.listar()

    def salvar(self, nome, email):
        if not nome or not nome.strip():
            return False, "O nome é obrigatório."

        ClienteModel.inserir(nome, email)
        return True, "Cliente cadastrado com sucesso."

    def atualizar(self, cliente_id, nome, email):
        if not nome or not nome.strip():
            return False, "O nome é obrigatório."

        ClienteModel.atualizar(cliente_id, nome, email)
        return True, "Cliente atualizado com sucesso."

    def excluir(self, cliente_id):
        ClienteModel.deletar(cliente_id)
        return True, "Cliente excluído com sucesso."
