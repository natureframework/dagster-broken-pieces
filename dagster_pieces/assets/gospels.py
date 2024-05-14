from typing import Dict
from pandas import DataFrame
from dagster import asset


@asset
def gospels(
    matthew: DataFrame, mark: DataFrame, luke: DataFrame, john: DataFrame
) -> Dict[str, DataFrame]:
    return {"matthew": matthew, "mark": mark, "luke": luke, "john": john}
