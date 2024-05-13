from dagster import asset
from dagster_pieces.partitions import partitions as partitions_def
from dagster_pieces.assets.partitions import partitions


@asset(partitions_def=partitions_def, deps=[partitions])
def pieces():
    pass
