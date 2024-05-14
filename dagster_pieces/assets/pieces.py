from pandas import DataFrame
from dagster import asset
from dagster_pieces.partitions.defs.references import references
from dagster_pieces.assets.partitions import partitions


@asset(partitions_def=references, deps=[partitions])
def pieces(matthew: DataFrame, mark: DataFrame, luke: DataFrame, john: DataFrame):
    pass
