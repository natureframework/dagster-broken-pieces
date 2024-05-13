from pandas import DataFrame, read_csv
from dagster import asset
from dagster_pieces.constants import PREFIX


@asset(key_prefix=PREFIX)
def references() -> DataFrame:
    return read_csv(
        "https://raw.githubusercontent.com"
        "/natureframework"
        "/broken-pieces"
        "/main"
        "/references.txt",
        names=["reference"],
    )
