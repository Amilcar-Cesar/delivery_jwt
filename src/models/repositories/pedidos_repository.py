from sqlite3 import Connection


class PedidosRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def pedidos(self, descricao, data, user_id):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''INSERT INTO pedidos
                    (descricao, data, user_id)
                VALUES
                    (?, ?, ?)''',
                    (descricao, data, user_id)
        )