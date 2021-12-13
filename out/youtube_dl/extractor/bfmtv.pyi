from ..utils import extract_attributes as extract_attributes
from .common import InfoExtractor as InfoExtractor

class BFMTVBaseIE(InfoExtractor):
    BRIGHTCOVE_URL_TEMPLATE: str

class BFMTVIE(BFMTVBaseIE):
    IE_NAME: str

class BFMTVLiveIE(BFMTVIE):
    IE_NAME: str

class BFMTVArticleIE(BFMTVBaseIE):
    IE_NAME: str
