from ..utils import int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class SprutoBaseIE(InfoExtractor): ...

class VimpleIE(SprutoBaseIE):
    IE_DESC: str
