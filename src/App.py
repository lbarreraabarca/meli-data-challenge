from com.data.factory.adapters.FileOperator import FileOperator
from com.data.factory.adapters.DataOperator import DataOperator
from com.data.factory.adapters.Results import Results

if __name__ == "__main__":
    file = FileOperator()
    data = DataOperator()
    result = Results(data)

    # df_pays = file.read("resources/data/pays.csv")
    df_prints = file.read("resources/data/prints.json")
    df_taps = file.read("resources/data/taps.json")

    # Casting and extracting columns for prints dataframe
    df_prints = data.cast_str_to_date(df_prints, "day", "%Y-%m-%d")
    df_prints = data.extract_field(df_prints, "event_data", "position")
    df_prints = data.extract_field(df_prints, "event_data", "value_prop")
    df_prints = data.drop_column(df_prints, "event_data")

    # Casting and extracting columns for taps dataframe
    df_taps = data.cast_str_to_date(df_taps, "day", "%Y-%m-%d")
    df_taps = data.extract_field(df_taps, "event_data", "position")
    df_taps = data.extract_field(df_taps, "event_data", "value_prop")
    df_taps = data.drop_column(df_taps, "event_data")

    print(df_taps)

    # Solutions
    df_1 = result.prints_last_week(df_prints)
