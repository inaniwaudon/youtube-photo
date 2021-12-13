from ..utils import determine_ext as determine_ext, mimetype2ext as mimetype2ext, parse_duration as parse_duration, qualities as qualities, try_get as try_get, url_or_none as url_or_none
from .common import InfoExtractor as InfoExtractor

class ImdbIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class ImdbListIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str
