class Config:
    db_config = {"user": "root",
                 "password": "root",
                 "host": "localhost",
                 "database": "dita"}

    table = None

    @classmethod
    def get_table(cls):
        return cls.table

    @classmethod
    def set_table(cls, table):
        cls.table = table