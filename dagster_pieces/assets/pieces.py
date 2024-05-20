from typing import Dict
from pandas import DataFrame
from referenceparser import parse
from dagster import AssetExecutionContext, asset
from dagster_pieces.partitions.defs.references import references
from dagster_pieces.select import select


@asset(partitions_def=references)
def pieces(context: AssetExecutionContext, gospels: Dict[str, DataFrame]) -> DataFrame:
    reference = parse(context.partition_key)
    book = gospels[reference.book]
    verses = select(book, reference)
    return verses
