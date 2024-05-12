from pandas import Series, read_csv
from dagster import asset


@asset
def references() -> Series:
    return read_csv(
        "https://raw.githubusercontent.com"
        "/natureframework"
        "/broken-pieces"
        "/main"
        "/references.txt",
        header=None,
    )[0]
