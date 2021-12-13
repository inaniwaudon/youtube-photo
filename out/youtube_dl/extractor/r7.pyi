from ..utils import int_or_none as int_or_none
from .common import InfoExtractor as InfoExtractor

class R7IE(InfoExtractor): ...

class R7ArticleIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
