import uuid


class UuidSupplier:
    def get(self):
        return str(uuid.uuid4())
