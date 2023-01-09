import unittest
import database as db


class HappDbExistance(unittest.TestCase):
    def setUp(self):
        # print(dir(self))
        self.sql = db.Sqlite("healthapp", "health")

    def test_methoddbdata2df(self):
        self.assertTrue(getattr(db, "dbdata2df", False))

    def test_dbexists(self):
        self.assertTrue(self.sql.exists_db())


class HappDbMethod(unittest.TestCase):
    def setUp(self):
        self.sql = db.Sqlite("healthapp", "health")

    def test_type_get_colnames(self):
        self.assertEqual(type(self.sql.get_colnames()), list)


# class Valuetest


# class TestStringMethods(unittest.TestCase):
#     def test_upper(self):
#         self.assertEqual("foo".upper(), "FOO")

#     def test_isupper(self):
#         self.assertTrue("FOO".isupper())
#         self.assertFalse("Foo".isupper())

# def test_split(self):
#     s = "hello world"
#     self.assertEqual(s.split(), ["hello", "world"])
#     # check that s.split fails when the separator is not a string
#     with self.assertRaises(TypeError):
#         s.split(2)


if __name__ == "__main__":
    # db.dbdata2df()
    # print(unittest.getTestCaseNames(Existancetest, "test"))
    # print(unittest.counts(Existancetest, "test"))
    # Existancetest
    unittest.main()
    # Importtest.importtest()
