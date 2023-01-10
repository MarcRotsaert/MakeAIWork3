import unittest
import database as db
import numpy as np


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

    def test_type_get_datafromcolumn(self):
        colnames = self.sql.get_colnames()
        for cname in colnames[1:]:
            self.assertIsInstance(self.sql.get_datafromcolumn(cname), np.ndarray)

    def test_type_get_data(self):
        self.assertEqual(len(self.sql.get_data()), 2)
        self.assertIsInstance(self.sql.get_data()[0], list)
        self.assertIsInstance(self.sql.get_data()[1], np.ndarray)


if __name__ == "__main__":
    # db.dbdata2df()
    # print(unittest.getTestCaseNames(Existancetest, "test"))
    # print(unittest.counts(Existancetest, "test"))
    # Existancetest
    unittest.main()
    # Importtest.importtest()
