import pandas as pd

class DataOperator():

    def cast_str_to_date(self,
                         df: pd.DataFrame,
                         column_name: str,
                         format: str):
        df[column_name] = pd.to_datetime(df[column_name], format=format)
        return df
