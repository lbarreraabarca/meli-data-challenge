import pandas as pd
from pandas.testing import assert_frame_equal
import unittest
from com.data.factory.adapters.FileOperator import FileOperator
from com.data.factory.adapters.DataOperator import DataOperator
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)


class testFileOperator(unittest.TestCase):

    def test_read_json(self):
        file = FileOperator()
        data = DataOperator()
        df = file.read("test/com/resources/data/x.json")
        data.extract_field(df, "event_data", "position")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
