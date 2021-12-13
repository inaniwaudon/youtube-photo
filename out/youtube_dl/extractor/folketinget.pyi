from ..compat import compat_parse_qs as compat_parse_qs
from ..utils import int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class FolketingetIE(InfoExtractor):
    IE_DESC: str
