from .user_repository import UserRepository
from src.models.settings.db_connection_handle import db_connection_handler
from unittest.mock import Mock

class MockCursor:
   def __init__(self):
      self.execute = Mock()
      self.fetchone = Mock()

class MockConnection:
   def __init__(self):
      self.cursor = Mock(return_value=MockCursor())
      self.commit = Mock()

def test_registry_user():
   username = "amilcar"
   password = "1234"

   mock_connection = MockConnection()
   repo = UserRepository(mock_connection)

   repo.create_user(username, password)

   cursor = mock_connection.cursor.return_value

   assert "INSERT INTO users" in cursor.execute.call_args[0][0]
   assert "(username, password)" in cursor.execute.call_args[0][0]
   assert "VALUES" in cursor.execute.call_args[0][0]
   assert cursor.execute.call_args[0][1] == (username, password)