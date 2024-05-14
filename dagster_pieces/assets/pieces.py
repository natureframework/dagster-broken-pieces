from pandas import DataFrame
from referenceparser import parse
from dagster import AssetExecutionContext, asset
from dagster_pieces.select.reference.select import select as select_verses
from dagster_pieces.select.book.select import select as select_book
from dagster_pieces.partitions.defs.references import references
from dagster_pieces.assets.partitions import partitions


@asset(partitions_def=references, deps=[partitions])
def pieces(
    context: AssetExecutionContext,
    matthew: DataFrame,
    mark: DataFrame,
    luke: DataFrame,
    john: DataFrame,
) -> DataFrame:
    reference = parse(context.partition_key)
    book = select_book(matthew, mark, luke, john, reference.book)
    verses = select_verses(book, reference)
    return verses
