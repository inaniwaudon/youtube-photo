from ..compat import compat_str as compat_str, compat_urlparse as compat_urlparse
from ..utils import determine_ext as determine_ext, find_xpath_attr as find_xpath_attr, float_or_none as float_or_none, int_or_none as int_or_none, orderedSet as orderedSet, parse_iso8601 as parse_iso8601, update_url_query as update_url_query, xpath_attr as xpath_attr, xpath_text as xpath_text, xpath_with_ns as xpath_with_ns
from .common import InfoExtractor as InfoExtractor

class LivestreamIE(InfoExtractor):
    IE_NAME: str

class LivestreamOriginalIE(InfoExtractor):
    IE_NAME: str

class LivestreamShortenerIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: bool
