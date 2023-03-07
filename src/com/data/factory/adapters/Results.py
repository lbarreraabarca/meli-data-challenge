from uuid import uuid4
from datetime import timedelta
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

    def prints_were_clicked(self,
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

    def get_number_times(self,
                         df_left: pd.DataFrame,
                         df_right: pd.DataFrame) -> pd.DataFrame:
        df_left = self.data.drop_column(df_left, "event_data_position")
        df_right = self.data.drop_column(df_right, "event_data_position")
        df_snapshot = df_left
        on_fieds = ["user_id", "event_data_value_prop"]
        df_join = pd.merge(df_left,
                           df_right,
                           how="left",
                           left_on=on_fieds,
                           right_on=on_fieds)

        df_join["three_weeks"] = df_join["day_x"] + timedelta(days=-21)

        filter = df_join["day_x"] > df_join["day_y"]
        filter_three_weeks = df_join["day_y"] > df_join["three_weeks"]
        df_join = df_join.where(filter) \
            .where(filter_three_weeks).dropna().reset_index()
        df_join = self.data.drop_column(df_join, "index")
        df_join["day"] = df_join["day_x"]

        # Group
        group_fields = ["day", "user_id", "event_data_value_prop"]
        df_join = df_join.groupby(group_fields)["day_y"] \
            .agg("count")

        df_join = self.data.drop_column(df_join, "three_weeks")
        df_join = self.data.drop_column(df_join, "day_y")
        df_join = self.data.drop_column(df_join, "day_x")

        # Temporal result
        tmp_file = f"/tmp/{str(uuid4())}.csv"
        df_join.to_csv(tmp_file)

        df_tmp = pd.read_csv(tmp_file)
        df_tmp = self.data.cast_str_to_date(df_tmp, "day", "%Y-%m-%d")

        # Left Join
        on_fieds = ["day", "user_id", "event_data_value_prop"]
        df_final = pd.merge(df_snapshot,
                            df_tmp,
                            how="left",
                            left_on=on_fieds,
                            right_on=on_fieds)
        df_final["number_times"] = df_final["day_y"] \
            .apply(lambda x: int(x) if x > 0 else int(0))
        df_final = self.data.drop_column(df_final, "day_y")
        return df_final

    @property
    def data(self) -> DataOperator:
        return self._data
