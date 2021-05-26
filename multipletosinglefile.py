from pandas import DataFrame, read_csv, read_json, concat
from pathlib import Path
from os import path, listdir

source_directory: str = "/Users/jagan/interview_assigment-1/input"
output_file: str = "/Users/jagan/interview_assigment-1/output/combine.csv"
unified_df: DataFrame = DataFrame()


def _read_source_file_to_df(file_path: str, file_format: str) -> DataFrame:
    """This method is to read data from path

    Args:
        file_path: path of the file
        file_format: format of the source file

    Returns:
        DataFrame: output of the file data in dataframe
    """
    if file_format == ".csv":
        return read_csv(file_path)
    elif file_format == ".json":
        return read_json(file_path)


if __name__ == "__main__":
    try:
        for filename in listdir(source_directory):
            file_path: str = path.join(source_directory, filename)
            file_format: str = Path(file_path).suffix
            df: DataFrame = _read_source_file_to_df(file_path, file_format)
            df["_source"] = file_path
            unified_df = concat([unified_df, df])
            unified_df.to_csv(output_file)
    except Exception as e:
        print(f"Error {e}")
