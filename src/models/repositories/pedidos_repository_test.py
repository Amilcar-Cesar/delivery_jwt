from .pedidos_repository import PedidosRepository
from unittest.mock import Mock
from datetime import date

class MockCursor:
   def __init__(self):
      self.execute = Mock()
      self.fetchone = Mock()

class MockConnection:
   def __init__(self):
      self.cursor = Mock(return_value=MockCursor())
      self.commit = Mock()

def test_pedidos():
   descricao = "haburg"
   data = date.today()
   user_id = 1

   mock_connection = MockConnection()
   repo = PedidosRepository(mock_connection)

   repo.pedidos(descricao, data, user_id)

   cursor = mock_connection.cursor.return_value

   assert "INSERT INTO pedidos" in cursor.execute.call_args[0][0]
   assert "(descricao, data, user_id)" in cursor.execute.call_args[0][0]
   assert "VALUES" in cursor.execute.call_args[0][0]
   assert cursor.execute.call_args[0][1] == (descricao, data, user_id)
