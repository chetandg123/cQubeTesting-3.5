import unittest


from reuse_func import GetData


class Database(unittest.TestCase):

    def test_database_username_password(self):
        self.cal = GetData()
        self.connection = self.cal.connect_to_postgres()
        if self.connection is not None:
            print("Database configured with provided username and password")
        else:
            raise self.failureException("Database is not configured with provided username and password")

