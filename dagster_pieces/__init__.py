from dagster import Definitions
from .assets.pieces import pieces
from .assets.partitions import partitions
from .assets.references import references

defs = Definitions(assets=[references, partitions, pieces])
