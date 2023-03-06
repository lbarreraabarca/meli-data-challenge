import pandas as pd


class FileOperator():

    def read(self, path: str) -> pd.DataFrame:
        path_splitted = path.split("/")
        format = str(path_splitted[len(path_splitted) - 1]).split(".")[1]
        if path is None or path == "":
            raise Exception("path cannot be None or empty.")
        if format is None or format == "":
            raise Exception("format cannot be None or empty.")
        if format == "json":
            return pd.read_json(path, lines=True)
        elif format == "csv":
            return pd.read_csv(path)
        else:
            raise Exception(f"{format} has not been implemented.")
