from ..utils import int_or_none as int_or_none, strip_or_none as strip_or_none, unescapeHTML as unescapeHTML, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class NTVRuIE(InfoExtractor):
    IE_NAME: str
