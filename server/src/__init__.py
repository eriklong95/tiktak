from src.flaskr.persistence.db_connection.db_connection_supplier import DatabaseConnectionSupplier

# Test classes are imported here to do automatic testing
# with the unittest framework easy to do from CLI.
from src.flaskr.test.serialization_test import TestUserSerialization, TestGameInputSerialization, TestGameSerialization, TestMoveSerialization
from src.flaskr.test.deserialization_test import TestUserDeserialization, TestGameInputDeserialization, TestGameDeserialization, TestMoveDeserialization
from src.flaskr.test.persistence.repositories.user_repository_test import TestUserInsertion, TestUserUpdate
from src.flaskr.test.persistence.repositories.game_repository_test import TestGameInsertion, TestMoveInsertion
from src.flaskr.test.turn_logic_test import TestTurnDerivation
from src.flaskr.test.winner_logic_test import TestFindWinner
