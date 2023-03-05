from datetime import datetime, timedelta
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

    @property
    def data(self) -> DataOperator:
        return self._data
