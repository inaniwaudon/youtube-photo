from ..compat import compat_urlparse as compat_urlparse
from ..utils import clean_html as clean_html, get_element_by_class as get_element_by_class, int_or_none as int_or_none, parse_iso8601 as parse_iso8601, remove_start as remove_start, unified_timestamp as unified_timestamp
from .common import InfoExtractor as InfoExtractor

class NextMediaIE(InfoExtractor):
    IE_DESC: str

class NextMediaActionNewsIE(NextMediaIE):
    IE_DESC: str

class AppleDailyIE(NextMediaIE):
    IE_DESC: str

class NextTVIE(InfoExtractor):
    IE_DESC: str
