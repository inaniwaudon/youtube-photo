from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, InAdvancePagedList as InAdvancePagedList, determine_ext as determine_ext, dict_get as dict_get, float_or_none as float_or_none, int_or_none as int_or_none, parse_duration as parse_duration, parse_iso8601 as parse_iso8601, remove_start as remove_start, try_get as try_get, unified_timestamp as unified_timestamp, urlencode_postdata as urlencode_postdata, xpath_text as xpath_text
from .common import InfoExtractor as InfoExtractor

class NiconicoIE(InfoExtractor):
    IE_NAME: str
    IE_DESC: str

class NiconicoPlaylistIE(InfoExtractor): ...
