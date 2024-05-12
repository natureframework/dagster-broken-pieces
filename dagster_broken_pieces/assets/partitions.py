from dagster import AssetExecutionContext, asset
from pandas import Series


@asset
def partitions(context: AssetExecutionContext, references: Series) -> None:
    context.instance.add_dynamic_partitions("references", references.to_list())
