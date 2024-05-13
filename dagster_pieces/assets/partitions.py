from dagster import AssetExecutionContext, asset
from pandas import DataFrame


@asset
def partitions(context: AssetExecutionContext, references: DataFrame) -> None:
    partition_keys = references["reference"].to_list()
    context.instance.add_dynamic_partitions("references", partition_keys)
