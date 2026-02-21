class MockDatabaseConnectionSupplier:
    def get(self):
        return MockDatabaseConnection()
    

# The classes below are used to mock the PEP 249 Python Database API

class MockDatabaseConnection:
    def close(self):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def cursor(self):
        return MockCursor()
    

class MockCursor:
    def close(self):
        pass

    def execute(self, operation, parameters):
        return self

    def executemany(self, operation, seq_of_parameters):
        return self

    def fetchone(self):
        return None

    def fetchmany(self):
        []

    def fetchall(self):
        []