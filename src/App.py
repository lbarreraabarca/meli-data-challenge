from com.data.factory.adapters.FileOperator import FileOperator
from com.data.factory.adapters.DataOperator import DataOperator
from com.data.factory.adapters.Results import Results
from com.data.factory.utils.logger import logging

LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    file = FileOperator()
    data = DataOperator()
    result = Results(data)

    LOG.info("Reading data sources.")
    df_pays = file.read("resources/data/pays.csv")
    df_prints = file.read("resources/data/prints.json")
    df_taps = file.read("resources/data/taps.json")

    LOG.info("Applying transforms to prints dataframe.")
    df_prints = data.cast_str_to_date(df_prints, "day", "%Y-%m-%d")
    df_prints = data.extract_field(df_prints, "event_data", "position")
    df_prints = data.extract_field(df_prints, "event_data", "value_prop")
    df_prints = data.drop_column(df_prints, "event_data")

    LOG.info("Applying transforms to taps dataframe.")
    df_taps = data.cast_str_to_date(df_taps, "day", "%Y-%m-%d")
    df_taps = data.extract_field(df_taps, "event_data", "position")
    df_taps = data.extract_field(df_taps, "event_data", "value_prop")
    df_taps = data.drop_column(df_taps, "event_data")

    LOG.info("Applying transforms to apys dataframe.")
    df_pays["day"] = df_pays["pay_date"]
    df_pays["event_data_value_prop"] = df_pays["value_prop"]
    df_pays = data.cast_str_to_date(df_pays, "day", "%Y-%m-%d")

    # Solutions
    LOG.info(f"Getting prints last week.")
    df_1 = result.prints_last_week(df_prints)
    LOG.info(f"Getting prints were clicked.")
    df_2 = result.prints_were_clicked(df_prints, df_taps)
    LOG.info(f"Getting prints that user has seen in last 3 weeks.")
    df_3 = result.get_number_times(df_prints, df_prints)
    LOG.info(f"Getting prints that user has clicked in last 3 weeks.")
    df_4 = result.get_number_times(df_prints, df_taps)
    LOG.info(f"Getting prints that user has paid in last 3 weeks.")
    df_5 = result.get_number_times(df_prints, df_pays)
    LOG.info(f"Getting prints that user has spent in last 3 weeks.")
    df_6 = result.get_number_times(df_prints,
                                   df_pays,
                                   operation_field="total",
                                   operation="sum")

    parent_output_path = "../output/"
    LOG.info(f"Writing solutions into {parent_output_path} folder.")
    df_1.to_csv(parent_output_path + "df_1.csv", index=False)
    df_2.to_csv(parent_output_path + "df_2.csv", index=False)
    df_3.to_csv(parent_output_path + "df_3.csv", index=False)
    df_4.to_csv(parent_output_path + "df_4.csv", index=False)
    df_5.to_csv(parent_output_path + "df_5.csv", index=False)
    df_6.to_csv(parent_output_path + "df_6.csv", index=False)
