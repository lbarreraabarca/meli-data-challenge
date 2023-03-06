import pandas as pd
from pandas.testing import assert_frame_equal
import unittest
from com.data.factory.adapters.Results import Results
from com.data.factory.adapters.DataOperator import DataOperator
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)


class testResults(unittest.TestCase):

    def test_click_by_print_1(self):
        data = DataOperator()
        result = Results(data)

        # Prints
        prints_rows = [{
                "day":"2020-11-01",
                "event_data_position": 1,
                "event_data_value_prop":"transport",
                "user_id": 1
            },
            {
                "day":"2020-11-01",
                "event_data_position": 2,
                "event_data_value_prop":"cellphone_recharge",
                "user_id": 2
            }
        ]
        df_prints = pd.DataFrame(prints_rows)

        # Taps
        taps_rows = [{
                "day": "2020-11-01",
                "event_data_position": 1,
                "event_data_value_prop": "transport",
                "user_id": 1
            }
        ]
        df_taps = pd.DataFrame(taps_rows)
        df_result = result.print_was_clicked(df_prints, df_taps)

        expected = [
            {
                "day": "2020-11-01",
                "event_data_value_prop": "transport",
                "user_id": 1,
                "clicked": True
            },
            {
                "day": "2020-11-01",
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 2,
                "clicked": False
            }
        ]
        df_expected = pd.DataFrame(expected)
        assert_frame_equal(df_expected, df_result)


if __name__ == '__main__':
    unittest.main()
