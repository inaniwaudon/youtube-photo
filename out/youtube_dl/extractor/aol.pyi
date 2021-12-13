from ..compat import compat_parse_qs as compat_parse_qs, compat_urllib_parse_urlparse as compat_urllib_parse_urlparse
from ..utils import ExtractorError as ExtractorError, int_or_none as int_or_none, url_or_none as url_or_none
from .yahoo import YahooIE as YahooIE

class AolIE(YahooIE):
    IE_NAME: str
