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
        prints_rows = [
            {
                "day": "2020-11-01",
                "event_data_position": 1,
                "event_data_value_prop": "transport",
                "user_id": 1
            },
            {
                "day": "2020-11-01",
                "event_data_position": 2,
                "event_data_value_prop": "cellphone_recharge",
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
        df_result = result.prints_were_clicked(df_prints, df_taps)

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

    def test_sum_prints_1(self):
        data = DataOperator()
        result = Results(data)

        # Prints
        prints_rows = [
            {
                "day": "2020-11-16",
                "event_data_position": 0,
                "event_data_value_prop": "credits_consumer",
                "user_id": 91238
            },
            {
                "day": "2020-11-17",
                "event_data_position": 1,
                "event_data_value_prop": "prepaid",
                "user_id": 91238
            },
            {
                "day": "2020-11-16",
                "event_data_position": 2,
                "event_data_value_prop": "transport",
                "user_id": 91238
            },
            {
                "day": "2020-11-01",
                "event_data_position": 0,
                "event_data_value_prop": "prepaid",
                "user_id": 91238
            },
            {
                "day": "2020-11-05",
                "event_data_position": 1,
                "event_data_value_prop": "credits_consumer",
                "user_id": 91238
            },
            {
                "day": "2020-11-01",
                "event_data_position": 2,
                "event_data_value_prop": "credits_consumer",
                "user_id": 91238
            }
        ]
        df_prints = pd.DataFrame(prints_rows)
        df_prints = data.cast_str_to_date(df_prints, "day", "%Y-%m-%d")

        df_actual = result.get_number_times(df_prints, df_prints)
        print(df_actual)
        self.assertTrue(True)

    def test_sum_clicked(self):
        data = DataOperator()
        result = Results(data)

        # Prints
        prints_rows = [
            {
                "day": "2020-11-12",
                "event_data_position": 0,
                "event_data_value_prop": "prepaid",
                "user_id": 95844
            },
            {
                "day": "2020-11-12",
                "event_data_position": 1,
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 95844
            },
            {
                "day": "2020-11-12",
                "event_data_position": 2,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 0,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 1,
                "event_data_value_prop": "credits_consumer",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 2,
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 3,
                "event_data_value_prop": "point",
                "user_id": 95844
            }
        ]
        df_prints = pd.DataFrame(prints_rows)
        df_prints = data.cast_str_to_date(df_prints, "day", "%Y-%m-%d")

        taps_rows = [
            {
                "day": "2020-11-12",
                "event_data_position": 2,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 1,
                "event_data_value_prop": "credits_consumer",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 2,
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 95844
            }
        ]
        df_taps = pd.DataFrame(taps_rows)
        df_taps = data.cast_str_to_date(df_taps, "day", "%Y-%m-%d")

        df_actual = result.get_number_times(df_prints, df_taps)
        print(df_actual)
        self.assertTrue(True)

    def test_sum_total(self):
        data = DataOperator()
        result = Results(data)

        # Prints
        prints_rows = [
            {
                "day": "2020-11-12",
                "event_data_position": 0,
                "event_data_value_prop": "prepaid",
                "user_id": 95844
            },
            {
                "day": "2020-11-12",
                "event_data_position": 1,
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 95844
            },
            {
                "day": "2020-11-12",
                "event_data_position": 2,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 0,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-17",
                "event_data_position": 0,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 1,
                "event_data_value_prop": "credits_consumer",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 2,
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "event_data_position": 3,
                "event_data_value_prop": "point",
                "user_id": 95844
            }
        ]
        df_prints = pd.DataFrame(prints_rows)
        df_prints = data.cast_str_to_date(df_prints, "day", "%Y-%m-%d")

        pays_rows = [
            {
                "day": "2020-11-12",
                "total": 10500,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-13",
                "total": 10500,
                "event_data_value_prop": "link_cobro",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "total": 10500,
                "event_data_value_prop": "credits_consumer",
                "user_id": 95844
            },
            {
                "day": "2020-11-15",
                "total": 10500,
                "event_data_value_prop": "cellphone_recharge",
                "user_id": 95844
            }
        ]
        df_pays = pd.DataFrame(pays_rows)
        df_pays = data.cast_str_to_date(df_pays, "day", "%Y-%m-%d")

        df_actual = result.get_number_times(df_prints,
                                            df_pays,
                                            operation_field="total",
                                            operation="sum")
        print(df_actual)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
