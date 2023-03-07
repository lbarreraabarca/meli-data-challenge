import pandas as pd
from pandas.testing import assert_frame_equal
import unittest
from com.data.factory.adapters.FileOperator import FileOperator
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)


class testFileOperator(unittest.TestCase):

    def test_read_json(self):
        file = FileOperator()
        df = file.read("test/com/resources/data/x.json")
        self.assertEqual(df["day"].size, 1)

    def test_read_json(self):
        file = FileOperator()
        df = file.read("test/com/resources/data/y.csv")
        self.assertEqual(df["day"].size, 1)

    def test_read_invalid_format(self):
        file = FileOperator()
        with self.assertRaises(Exception) as e:
            file.read("test/com/resources/data/a.fake")

    def test_read_invalid_format_2(self):
        file = FileOperator()
        with self.assertRaises(Exception) as e:
            file.read("test/com/resources/data/invalid;")

    def test_read_invalid_path_is_none(self):
        file = FileOperator()
        with self.assertRaises(Exception) as e:
            file.read(None)

    def test_read_invalid_path_is_empty(self):
        file = FileOperator()
        with self.assertRaises(Exception) as e:
            file.read("")


if __name__ == '__main__':
    unittest.main()
