import pandas as pd


class DataOperator():

    def cast_str_to_date(self,
                         df: pd.DataFrame,
                         column_name: str,
                         format: str):
        df[column_name] = pd.to_datetime(df[column_name], format=format)
        return df

    def extract_field(self,
                      df: pd.DataFrame,
                      parent_column_name: str,
                      extracted_column_name: str) -> pd.DataFrame:
        new_column_name = f"{parent_column_name}_{extracted_column_name}"
        df[new_column_name] = df[parent_column_name] \
            .apply(lambda x: x[extracted_column_name])
        return df

    def drop_column(self,
                    df: pd.DataFrame,
                    column_name: str) -> pd.DataFrame:
        return df.drop(columns=[column_name])
