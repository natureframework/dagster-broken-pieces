from dagster import Definitions
from .assets.broken_pieces import broken_pieces
from .assets.partitions import partitions
from .assets.references import references

defs = Definitions(assets=[references, partitions, broken_pieces])
