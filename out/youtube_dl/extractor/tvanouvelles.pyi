from .brightcove import BrightcoveNewIE as BrightcoveNewIE
from .common import InfoExtractor as InfoExtractor

class TVANouvellesIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str

class TVANouvellesArticleIE(InfoExtractor):
    @classmethod
    def suitable(cls, url): ...
