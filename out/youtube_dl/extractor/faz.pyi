from ..compat import compat_etree_fromstring as compat_etree_fromstring
from ..utils import int_or_none as int_or_none, xpath_element as xpath_element, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class FazIE(InfoExtractor):
    IE_NAME: str
