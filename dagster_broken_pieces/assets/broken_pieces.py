from dagster import asset
from dagster_broken_pieces.partitions.references import references
from dagster_broken_pieces.assets.partitions import partitions


@asset(partitions_def=references, deps=[partitions])
def broken_pieces():
    pass
