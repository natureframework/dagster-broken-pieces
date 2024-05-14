from dagster import AssetExecutionContext, asset
from pandas import DataFrame
from dagster_pieces.partitions.reset import reset


@asset
def partitions(context: AssetExecutionContext, references: DataFrame) -> None:
    keys = references["reference"].to_list()
    reset(context.instance, "references", keys)
