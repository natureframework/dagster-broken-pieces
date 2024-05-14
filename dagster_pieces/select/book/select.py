from pandas import DataFrame


def select(
    matthew: DataFrame, mark: DataFrame, luke: DataFrame, john: DataFrame, book: str
) -> DataFrame:
    if book == "matthew":
        return matthew
    if book == "mark":
        return mark
    if book == "luke":
        return luke
    if book == "john":
        return john
    raise ValueError(f"Invalid book: {book}")
