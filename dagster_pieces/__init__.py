from dagster import Definitions
from .assets.partitions import partitions
from .assets.references import references
from .assets.gospels import gospels
from .assets.matthew import matthew
from .assets.piece import piece
from .assets.mark import mark
from .assets.luke import luke
from .assets.john import john

defs = Definitions(
    assets=[references, partitions, matthew, mark, luke, john, gospels, piece]
)
