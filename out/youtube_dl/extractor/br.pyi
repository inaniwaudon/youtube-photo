from ..utils import ExtractorError as ExtractorError, determine_ext as determine_ext, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, xpath_element as xpath_element, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class BRIE(InfoExtractor):
    IE_DESC: str

class BRMediathekIE(InfoExtractor):
    IE_DESC: str
