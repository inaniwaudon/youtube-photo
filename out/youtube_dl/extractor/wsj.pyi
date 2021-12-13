from ..utils import float_or_none as float_or_none, int_or_none as int_or_none, unified_strdate as unified_strdate
from .common import InfoExtractor as InfoExtractor

class WSJIE(InfoExtractor):
    IE_DESC: str

class WSJArticleIE(InfoExtractor): ...
