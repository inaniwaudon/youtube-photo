from .common import InfoExtractor as InfoExtractor
from .vimple import SprutoBaseIE as SprutoBaseIE

class MyviIE(SprutoBaseIE): ...

class MyviEmbedIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
