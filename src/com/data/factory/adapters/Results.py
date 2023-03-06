from datetime import datetime, timedelta
import numpy as np
import pandas as pd
from com.data.factory.adapters.DataOperator import DataOperator


class Results():

    def __init__(self, data: DataOperator) -> None:
        self._data = data

    def prints_last_week(self, df: pd.DataFrame) -> pd.DataFrame:
        max_day = df["day"].max()
        sub_one_week = max_day + timedelta(days=-7)
        filter = df["day"] >= sub_one_week
        return df.where(filter).dropna().reset_index()

    def print_was_clicked(self,
                       df_prints: pd.DataFrame,
                       df_taps: pd.DataFrame) -> pd.DataFrame:
        on_fieds = ["user_id", "day", "event_data_value_prop"]
        df_result = pd.merge(df_prints,
                             df_taps,
                             how="left",
                             left_on=on_fieds,
                             right_on=on_fieds)
        df_result['clicked'] = df_result['event_data_position_y'] \
            .apply(lambda x: not pd.isnull(x))
        df_result = self.data.drop_column(df_result, "event_data_position_x")
        df_result = self.data.drop_column(df_result, "event_data_position_y")
        return df_result

    @property
    def data(self) -> DataOperator:
        return self._data
