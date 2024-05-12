from pandas import DataFrame, read_csv
from dagster import asset


@asset
def references() -> DataFrame:
    return read_csv(
        "https://raw.githubusercontent.com"
        "/natureframework"
        "/broken-pieces"
        "/main"
        "/references.txt",
        names=["reference"],
    )
