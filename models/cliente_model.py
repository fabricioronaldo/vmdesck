from database.db import get_connection

class ClienteModel:

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome, email FROM clientes")
        dados = cursor.fetchall()
        conn.close()
        return dados

    @staticmethod
    def inserir(nome, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def atualizar(cliente_id, nome, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nome=?, email=? WHERE id=?",
            (nome, email, cliente_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def deletar(cliente_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id=?", (cliente_id,))
        conn.commit()
        conn.close()
