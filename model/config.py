class Config:
    db_config = {"user": "root",
                 "password": "root",
                 "host": "localhost",
                 "database": "dita"}

    collection = None

    @classmethod
    def get_collection(cls):
        return cls.collection

    @classmethod
    def set_collection(cls, collection):
        cls.table = collection