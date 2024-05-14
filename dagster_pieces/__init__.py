from dagster import Definitions
from .assets.pieces import pieces
from .assets.partitions import partitions
from .assets.references import references
from .assets.matthew import matthew
from .assets.mark import mark
from .assets.luke import luke
from .assets.john import john

defs = Definitions(assets=[references, partitions, matthew, mark, luke, john, pieces])
