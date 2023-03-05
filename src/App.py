from com.data.factory.adapters.FileOperator import FileOperator
from com.data.factory.adapters.DataOperator import DataOperator


if __name__ == "__main__":
    file = FileOperator()
    data = DataOperator()

    #df_pays = file.read("resources/data/pays.csv")
    df_prints = file.read("resources/data/prints.json")
    #df_taps = file.read("resources/data/taps.json")
    df_prints = data.cast_str_to_date(df_prints, "day", "%Y-%m-%d")

    
    print(df_prints["day"].max())
