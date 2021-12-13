from ..utils import int_or_none as int_or_none, parse_iso8601 as parse_iso8601, xpath_attr as xpath_attr, xpath_element as xpath_element
from .common import InfoExtractor as InfoExtractor

class TwentyFourVideoIE(InfoExtractor):
    IE_NAME: str
