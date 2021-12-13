from ..utils import int_or_none as int_or_none, try_get as try_get
from .common import InfoExtractor as InfoExtractor

class CBSSportsEmbedIE(InfoExtractor):
    IE_NAME: str

class CBSSportsBaseIE(InfoExtractor): ...

class CBSSportsIE(CBSSportsBaseIE):
    IE_NAME: str

class TwentyFourSevenSportsIE(CBSSportsBaseIE):
    IE_NAME: str
