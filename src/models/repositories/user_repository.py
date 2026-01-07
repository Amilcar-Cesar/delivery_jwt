from sqlite3 import Connection

class UserRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''INSERT INTO users
                    (username, password)
                VALUES
                    (?, ?)''',
                    (username, password)
        )

